from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count

from cpovc_forms.forms import OVCSearchForm
from cpovc_forms.functions import get_person_ids
from .models import AFCMain, AFCEvents, AFCForms
from .forms import (
    AltCareForm, AFCForm1A, AFCForm1B, AFCForm2A, AFCForm4A, AFCForm5A,
    AFCForm6A, AFCForm7A, AFCForm8A, AFCForm9A, AFCForm10A,
    AFCForm12A, AFCForm14A, AFCForm15A, AFCForm16A)
from cpovc_registry.models import (
    RegPerson, RegPersonsSiblings, RegPersonsExternalIds, RegPersonsGeo)
from cpovc_forms.models import OVCCaseRecord, OVCCaseCategory
from cpovc_main.functions import get_dict
from .functions import (
    handle_alt_care, save_altcare_form, get_area, get_class_levels,
    get_education, get_form_info)
from .settings import FMS, CTS

# from cpovc_ovc.decorators import validate_ovc


@login_required
def alt_care_home(request):
    '''
    Some default page for forms home page
    '''
    try:
        form = OVCSearchForm(data=request.GET)
        # form = SearchForm(data=request.POST)
        # person_type = 'TBVC'
        afc_ids, case_ids = {}, {}
        search_string = request.GET.get('search_name')
        pids = get_person_ids(request, search_string)
        cases = RegPerson.objects.filter(is_void=False, id__in=pids)
        # Get case record sheet details
        crss = OVCCaseRecord.objects.filter(is_void=False, person_id__in=pids)
        for crs in crss:
            case_ids[crs.person_id] = {'clv': 1, 'cid': crs.case_id}
        # Check if there is a filled AFC Form
        afcs = AFCMain.objects.filter(is_void=False, person_id__in=pids)
        for afc in afcs:
            afc_ids[afc.person_id] = {'cid': afc.care_id,
                                      'clv': 2, 'cdt': afc.case_date}
        for case in cases:
            pid = case.id
            cid = afc_ids[pid]['cid'] if pid in afc_ids else 'N/A'
            cdt = afc_ids[pid]['cdt'] if pid in afc_ids else 'N/A'
            clvf = case_ids[pid]['clv'] if pid in case_ids else 0
            crs_id = case_ids[pid]['cid'] if pid in case_ids else None
            clv = afc_ids[pid]['clv'] if pid in afc_ids else clvf
            setattr(case, 'case_t', str(cid))
            setattr(case, 'care_id', cid)
            setattr(case, 'case_date', cdt)
            setattr(case, 'case_level', clv)
            setattr(case, 'case_id', crs_id)
        return render(request, 'afc/home.html',
                      {'status': 200, 'cases': cases, 'form': form})
    except Exception as e:
        raise e


@login_required
def new_alternative_care(request, case_id):
    '''
    New Alternative Care main page
    '''
    try:
        form = AltCareForm(initial={'person_type': 'TBVC'})
        check_fields = ['sex_id', 'case_category_id']
        vals = get_dict(field_name=check_fields)
        # Case Categories
        case = OVCCaseRecord.objects.get(case_id=case_id)
        categories = OVCCaseCategory.objects.filter(case_id_id=case_id)

        if request.method == 'POST':
            afc_params = {}
            person_id = case.person_id
            afc_params['case_id'] = case_id
            afc_params['person_id'] = person_id
            care_id = handle_alt_care(request, 0, afc_params)
            url = reverse(view_alternative_care, kwargs={'care_id': care_id})
            msg = 'Alternative Care details saved successfully'
            messages.add_message(request, messages.INFO, msg)
            return HttpResponseRedirect(url)
        return render(request, 'afc/new_alternative_care.html',
                      {'status': 200, 'case_id': case_id, 'vals': vals,
                       'categories': categories, 'case': case,
                       'form': form})
    except Exception as e:
        raise e


@login_required
def view_alternative_care(request, care_id):
    '''
    View Alternative Care main page
    '''
    try:
        case = AFCMain.objects.get(is_void=False, care_id=care_id)
        cid = str(case.care_type)[2:]
        cname = CTS[cid] if cid in CTS else 'Adoption'
        check_fields = ['sex_id', 'case_category_id',
                        'alternative_family_care_type_id',
                        'care_admission_reason_id']
        vals = get_dict(field_name=check_fields)
        # Events
        events = (AFCEvents.objects
                  .filter(care_id=care_id)
                  .values('form_id')
                  .annotate(dcount=Count('form_id'))
                  .order_by()
                  )
        # Common data
        fdatas = get_form_info(request, case.pk, case.person_id, False)
        forms = {}
        for event in events:
            forms[str(event['form_id'])] = event['dcount']
        return render(request, 'afc/view_alternative_care.html',
                      {'status': 200, 'case': case, 'vals': vals,
                       'cid': cid, 'care_name': cname, 'events': forms,
                       'fdatas': fdatas})
    except Exception as e:
        raise e


@login_required
def edit_alternative_care(request, care_id):
    '''
    Edit Alternative Care main page
    '''
    try:
        case = AFCMain.objects.get(is_void=False, care_id=care_id)
        cid = str(case.care_type)[2:]
        case_id = case.case_id
        if request.method == 'POST':
            afc_params = {}
            person_id = case.person_id
            afc_params['care_id'] = care_id
            afc_params['person_id'] = person_id
            handle_alt_care(request, 0, afc_params)
            url = reverse(view_alternative_care, kwargs={'care_id': care_id})
            msg = 'Alternative Care details updated successfully'
            messages.add_message(request, messages.INFO, msg)
            return HttpResponseRedirect(url)
        initial_info = {}
        cdate = case.case_date
        case_date = cdate.strftime('%d-%b-%Y')
        initial_info['care_option'] = case.care_type
        initial_info['case_date'] = case_date
        # Get common elements
        fdatas = get_form_info(request, case.pk, case.person_id, False)
        if fdatas:
            for fdt in fdatas:
                initial_info[fdt] = fdatas[fdt]
        form = AltCareForm(initial=initial_info)
        cname = CTS[cid] if cid in CTS else 'Adoption'
        check_fields = ['sex_id', 'case_category_id',
                        'alternative_family_care_type_id']
        vals = get_dict(field_name=check_fields)
        categories = OVCCaseCategory.objects.filter(case_id_id=case_id)
        return render(request, 'afc/edit_alternative_care.html',
                      {'status': 200, 'case': case, 'vals': vals,
                       'cid': cid, 'care_name': cname,
                       'form': form, 'categories': categories})
    except Exception as e:
        raise e


@login_required
def alt_care_form(request, cid, form_id, care_id, ev_id=0):
    '''
    Some default page for CTiP forms home page
    '''
    try:
        check_fields = ['sex_id', 'case_category_id', 'religion_type_id',
                        'alternative_family_care_type_id']
        vals = get_dict(field_name=check_fields)
        # Handle saved items
        events = AFCEvents.objects.filter(
            care_id=care_id, form_id=form_id)
        # print('Event', form_id, case_id, events)
        idata = {}
        if events:
            edate = events[0].event_date
            event_date = edate.strftime('%d-%b-%Y')
            idata['event_date'] = event_date
            event_id = events[0].pk
            fdatas = AFCForms.objects.filter(event_id=event_id)
            for fdata in fdatas:
                qid = fdata.question_id
                q_item = fdata.item_value
                q_detail = fdata.item_detail
                if qid.endswith('_txt'):
                    idata[qid] = q_detail
                elif qid.endswith('_rdo') or qid.endswith('_sdd'):
                    idata[qid] = q_item
                else:
                    if qid not in idata:
                        idata[qid] = []
                    idata[qid].append(q_item)
            print('idata', idata)
        form_name = FMS[form_id] if form_id in FMS else 'Default'
        case = AFCMain.objects.get(is_void=False, care_id=care_id)
        person_id = case.person_id
        case_id = case.case_id
        afcs = AFCMain.objects.filter(person_id=person_id)
        print('afcs', afcs)
        # Get education
        sch_class = ''
        ed = get_education(person_id)
        if ed:
            sch_class = ed.school_class
            idata['school_level'] = ed.school_level
            idata['school'] = ed.school_id
            idata['school_name'] = ed.school.school_name
            idata['school_class'] = sch_class
            idata['admission_type'] = ed.admission_type
        # Get persons registry info
        geos = {}
        geo_locs = RegPersonsGeo.objects.filter(
            person_id=person_id, is_void=False)
        for geo in geo_locs:
            geos[geo.area.area_type_id] = geo.area.area_name
            if geo.area.area_type_id == 'GDIS':
                a_id = geo.area.parent_area_id
                a_name = get_area(a_id)
                geos['GPRV'] = a_name
        # Class levels
        levels = get_class_levels()
        siblings = RegPersonsSiblings.objects.select_related().filter(
            child_person=person_id, is_void=False, date_delinked=None)
        extids = RegPersonsExternalIds.objects.filter(
            person_id=person_id, is_void=False)
        ext_ids = {}
        for extid in extids:
            ext_ids[str(extid.identifier_type_id)] = extid.identifier
        # Save submitted records
        if request.method == 'POST':
            res = save_altcare_form(request, form_id)
            if res:
                url = reverse(
                    view_alternative_care, kwargs={'care_id': care_id})
            msg = 'Form - %s saved successfully' % (form_id)
            messages.add_message(request, messages.INFO, msg)
            return HttpResponseRedirect(url)
        print('idata', idata)
        form = get_form(form_id, idata)
        tmpl = 'afc/new_form_%s.html' % (form_id)
        case_uid = str(case_id).replace('-', '')
        case_num = '%s/%s' % (str(case.case_number).zfill(6), 2022)
        return render(request, tmpl,
                      {'status': 200, 'case': case, 'form_id': form_id,
                       'form_name': form_name, 'vals': vals, 'geos': geos,
                       'form': form, 'case_id': case_uid, 'cid': cid,
                       'siblings': siblings, 'ext_ids': ext_ids,
                       'levels': levels, 'sch_class': sch_class,
                       'case_num': case_num, 'afcs': afcs})
    except Exception as e:
        raise e


def get_form(form_id, initial_data):
    """ Get the forms by ids."""
    try:
        form = AltCareForm(initial=initial_data)
        if form_id == '1A':
            form = AFCForm1A(initial=initial_data)
        elif form_id == '1B':
            form = AFCForm1B(initial=initial_data)
        elif form_id == '2A':
            form = AFCForm2A(initial=initial_data)
        elif form_id == '4A':
            form = AFCForm4A(initial=initial_data)
        elif form_id == '5A':
            form = AFCForm5A(initial=initial_data)
        elif form_id == '6A':
            form = AFCForm6A(initial=initial_data)
        elif form_id == '7A':
            form = AFCForm7A(initial=initial_data)
        elif form_id == '8A':
            form = AFCForm8A(initial=initial_data)
        elif form_id == '9A':
            form = AFCForm9A(initial=initial_data)
        elif form_id == '10A':
            form = AFCForm10A(initial=initial_data)
        elif form_id == '12A':
            form = AFCForm12A(initial=initial_data)
        elif form_id == '14A':
            form = AFCForm14A(initial=initial_data)
        elif form_id == '15A':
            form = AFCForm15A(initial=initial_data)
        elif form_id == '16A':
            form = AFCForm16A(initial=initial_data)
    except Exception as e:
        raise e
    else:
        return form
