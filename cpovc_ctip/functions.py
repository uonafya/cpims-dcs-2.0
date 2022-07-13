from django.shortcuts import get_object_or_404
from cpovc_main.functions import get_dict, convert_date
from .models import CTIPMain, CTIPEvents, CTIPForms


def handle_ctip(request, action, params={}):
    """Method to handle CTiP"""
    try:
        if action == 0:
            save_case(request, params)
    except Exception as e:
        print('Error saving TIP Action %s' % (str(e)))
    else:
        return True


def save_case(request, params):
    """Method to save Main case data."""
    try:
        case_id = params['case_id']
        person_id = params['person_id']
        case_date = params['case_date']
        obj, created = CTIPMain.objects.update_or_create(
            case_id=case_id,
            defaults={'case_date': case_date, 'person_id': person_id},
        )
    except Exception as e:
        print('Error saving TIP %s' % (str(e)))
    else:
        return True


def save_ctip_form(request, form_id):
    """Method to save forms."""
    try:
        response = True
        case_id = request.POST.get('case_id')
        person_id = request.POST.get('person_id')
        event_date = request.POST.get('event_date')
        if form_id == 'A':
            consent_date = request.POST.get('consent_date')
            has_consent = request.POST.get('has_consent')
            case = get_object_or_404(
                CTIPMain, case_id=case_id, is_void=False)
            case.has_consent = True if has_consent == 'AYES' else False
            case.consent_date = convert_date(consent_date)
            case.save(update_fields=["consent_date", "has_consent"])
        else:
            obj, created = CTIPEvents.objects.update_or_create(
                case_id=case_id, form_id=form_id,
                defaults={'event_date': convert_date(event_date),
                          'person_id': person_id})
            event_id = obj.pk
            save_form_data(request, form_id, event_id)
        pref = 'qf%s' % (form_id)
        extract_params(request, pref)
    except Exception as e:
        print('Error saving form - %s' % (str(e)))
        return False
    else:
        return response


def save_form_data(request, form_id, event_id):
    """Method to save Main forms data."""
    try:
        print('event id', event_id)
        form_pref = 'qf%s' % (form_id)
        all_itms = extract_params(request, form_pref)
        for itms in all_itms:
            for itm in all_itms[itms]:
                print('itm', itms, itm)
                itdm = 'QTXT' if itms.endswith('_txt') else itm
                itdl = itm if itms.endswith('_txt') else None
                print('itm after', itms, itm, itdl)
                obj, created = CTIPForms.objects.update_or_create(
                    event_id=event_id, question_id=itms,
                    item_value=itdm,
                    defaults={'item_value': itdm, 'item_detail': itdl},
                )
    except Exception as e:
        print('Error saving TIP %s' % (str(e)))
    else:
        return True


def extract_params(request, pref):
    """Method to extract charges items."""
    try:
        params, itms = {}, []
        for itm in request.POST:
            if itm.startswith(pref):
                itms.append(itm.replace(pref, ''))
        # print('items', itms)

        for dt in itms:
            itm_id = '%s%s' % (pref, dt)
            itm_value = request.POST.getlist(itm_id)
            if itm_value[0]:
                params[itm_id] = itm_value
        print(params)
    except Exception as e:
        print('Error getting charges - %s' % (e))
        return []
    else:
        return params
