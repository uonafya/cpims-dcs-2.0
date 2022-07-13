from datetime import datetime
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count

from cpovc_main.functions import get_dict
from cpovc_forms.models import OVCCaseCategory
from cpovc_forms.forms import OVCSearchForm
from cpovc_forms.functions import get_person_ids
from cpovc_registry.models import RegPersonsExternalIds
from .models import CTIPMain, CTIPEvents, CTIPForms
from .settings import FMS
from .forms import (
    CTIPFormA, CTIPFormB, CTIPFormC, CTIPFormD,
    CTIPFormE, CTIPFormF, CTIPFormG)
from .functions import save_ctip_form


@login_required
def ctip_home(request):
    '''
    Some default page for forms home page
    '''
    try:
        form = OVCSearchForm(data=request.GET)
        # form = SearchForm(data=request.POST)
        # person_type = 'TBVC'
        search_string = request.GET.get('search_name')
        pids = get_person_ids(request, search_string)
        cases = CTIPMain.objects.filter(is_void=False, person_id__in=pids)
        return render(request, 'ctip/home.html',
                      {'status': 200, 'cases': cases, 'form': form})
    except Exception as e:
        raise e


@login_required
def view_ctip_case(request, case_id):
    '''
    View CTiP main page
    '''
    try:
        # form = OVCSearchForm(initial={'person_type': 'TBVC'})
        check_fields = ['sex_id', 'case_category_id']
        vals = get_dict(field_name=check_fields)
        case = CTIPMain.objects.get(is_void=False, case_id=case_id)
        # Case Categories
        categories = OVCCaseCategory.objects.filter(case_id_id=case_id)
        events = (CTIPEvents.objects
                  .filter(case_id=case_id)
                  .values('form_id')
                  .annotate(dcount=Count('form_id'))
                  .order_by()
                  )
        print('events', events)
        ev_id = str(case.case.case_id).replace('-', '')
        forms = {}
        for event in events:
            forms[str(event['form_id'])] = event['dcount']
        print('forms', forms)
        return render(request, 'ctip/view_case.html',
                      {'status': 200, 'case': case, 'vals': vals,
                       'categories': categories, 'events': forms,
                       'ev_id': ev_id})
    except Exception as e:
        raise e


@login_required
def view_ctip_form(request, form_id, case_id):
    '''
    Some default page for CTiP forms home page
    '''
    try:
        check_fields = ['sex_id', 'case_category_id']
        vals = get_dict(field_name=check_fields)
        form_name = FMS[form_id] if form_id in FMS else 'Default'
        case = CTIPMain.objects.get(is_void=False, case_id=case_id)
        person_id = case.person.id
        contacts = RegPersonsExternalIds.objects.filter(person_id=person_id)
        # Check events
        idata = {}
        events = CTIPEvents.objects.filter(
            case_id=case_id, form_id=form_id)
        print('Event', form_id, case_id, events)
        if events:
            edate = events[0].event_date
            event_date = edate.strftime('%d-%b-%Y')
            idata['event_date'] = event_date
            event_id = events[0].pk
            fdatas = CTIPForms.objects.filter(event_id=event_id)
            for fdata in fdatas:
                qid = fdata.question_id
                q_item = fdata.item_value
                q_detail = fdata.item_detail
                if qid.endswith('_txt'):
                    idata[qid] = q_detail
                elif qid.endswith('_rdo'):
                    idata[qid] = q_item
                else:
                    if qid not in idata:
                        idata[qid] = []
                    idata[qid].append(q_item)
            print('idata', idata)
        form = get_form(form_id, idata)
        if request.method == 'POST':
            form.data = request.POST
            res = save_ctip_form(request, form_id)
            if res:
                url = reverse(view_ctip_case, kwargs={'case_id': case_id})
            else:
                url = reverse(view_ctip_form, kwargs={'form_id': form_id,
                                                      'case_id': case_id})
            msg = 'Form - %s saved successfully' % (form_id)
            messages.add_message(request, messages.INFO, msg)
            return HttpResponseRedirect(url)
        tmpl = 'ctip/view_form_%s.html' % (form_id)
        cid = str(case_id).replace('-', '')
        mydate = datetime.now()
        dtm = mydate.strftime("%d-%b-%Y (%I:%M:%S %p)")
        return render(request, tmpl,
                      {'status': 200, 'case': case, 'form_id': form_id,
                       'form_name': form_name, 'vals': vals,
                       'form': form, 'case_id': cid, 'events': events,
                       'contacts': contacts, 'datetime': dtm})
    except Exception as e:
        raise e


@login_required
def ctip_form(request, form_id, case_id):
    '''
    Some default page for CTiP forms home page
    '''
    try:
        check_fields = ['sex_id', 'case_category_id']
        vals = get_dict(field_name=check_fields)
        form_name = FMS[form_id] if form_id in FMS else 'Default'
        case = CTIPMain.objects.get(is_void=False, case_id=case_id)
        person_id = case.person.id
        contacts = RegPersonsExternalIds.objects.filter(person_id=person_id)
        # Forms and initial data
        has_consent = 'AYES' if case.has_consent else 'ANNO'
        cdate = case.consent_date
        if cdate:
            consent_date = cdate.strftime('%d-%b-%Y')
        else:
            consent_date = None
        if form_id == 'A':
            form = CTIPFormA(
                initial={'consent_date': consent_date,
                         'has_consent': has_consent})
        else:
            # Check events
            idata = {}
            events = CTIPEvents.objects.filter(
                case_id=case_id, form_id=form_id)
            print('Event', form_id, case_id, events)
            if events:
                edate = events[0].event_date
                event_date = edate.strftime('%d-%b-%Y')
                idata['event_date'] = event_date
                event_id = events[0].pk
                fdatas = CTIPForms.objects.filter(event_id=event_id)
                for fdata in fdatas:
                    qid = fdata.question_id
                    q_item = fdata.item_value
                    q_detail = fdata.item_detail
                    if qid.endswith('_txt'):
                        idata[qid] = q_detail
                    elif qid.endswith('_rdo'):
                        idata[qid] = q_item
                    else:
                        if qid not in idata:
                            idata[qid] = []
                        idata[qid].append(q_item)
                print('idata', idata)
            form = get_form(form_id, idata)
        if request.method == 'POST':
            form.data = request.POST
            res = save_ctip_form(request, form_id)
            if res:
                url = reverse(view_ctip_case, kwargs={'case_id': case_id})
            else:
                url = reverse(view_ctip_form, kwargs={'form_id': form_id,
                                                      'case_id': case_id})
            msg = 'Form - %s saved successfully' % (form_id)
            messages.add_message(request, messages.INFO, msg)
            return HttpResponseRedirect(url)
        tmpl = 'ctip/new_form_%s.html' % (form_id)
        cid = str(case_id).replace('-', '')
        return render(request, tmpl,
                      {'status': 200, 'case': case, 'form_id': form_id,
                       'form_name': form_name, 'vals': vals,
                       'form': form, 'case_id': cid, 'contacts': contacts})
    except Exception as e:
        raise e


def get_form(form_id, idata):
    """Method to get form."""
    try:
        if form_id == 'B':
            form = CTIPFormB(initial=idata)
        elif form_id == 'C':
            form = CTIPFormC(initial=idata)
        elif form_id == 'D':
            form = CTIPFormD(initial=idata)
        elif form_id == 'E':
            form = CTIPFormE(initial=idata)
        elif form_id == 'F':
            form = CTIPFormF(initial=idata)
        else:
            form = CTIPFormG(initial=idata)
    except Exception as e:
        raise e
    else:
        return form
