from django import forms
from django.forms.widgets import RadioFieldRenderer
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from cpovc_main.functions import get_list
immunization_list = get_list('immunization_status_id', 'Please Select')

person_type_list = get_list('person_type_id', 'Please Select Type')
school_level_list = get_list('school_level_id', 'Please Select Level')
admission_list = get_list('school_type_id', 'Please Select one')
disability_list = get_list('disability_type_id', 'Please Select one')
severity_list = get_list('severity_level_id', 'Please Select one')
admission_type_list = get_list('admission_type_id', 'Please Select')
admission_reason_list = get_list('care_admission_reason_id')
domain_list = get_list('olmis_domain_id', 'Please Select')
list_sex_id = get_list('sex_id')
consent_forms_list = get_list('consent_forms', 'Please Select')
# new listings
list_other_adms = get_list('other_form_admission', 'Please Select')
list_other_vulnerability = get_list(
    'vulnerability_at_admission', 'Please Select')
list_relationship = get_list('relationship_type_id', 'Please Select')
list_education_perf = get_list('education_performance')
list_marriage_type = get_list('parents_marriage_type')
list_items_count = get_list('items_count_id', 'Please Select')
list_special_support = get_list('special_support')
list_community_services = get_list('community_services')
list_school_category = get_list('school_category_id', 'Please Select')
list_range_level = get_list('attachment_level', 'Please Select')
list_child_exhibits = get_list('child_exhibits')
list_income_range = get_list('income_range', 'Please Select')
list_employment_type = get_list('employment_type', 'Please Select')
list_closure_reasons = get_list('case_closure_reasons', 'Please Select')
list_case_transfer_ids = get_list('case_transfer_ids', 'Please Select')
list_satisfied_level = get_list('satisfied_level_ids')
list_feeling_level = get_list('feeling_level_ids')
list_referral_reasons = get_list('referral_reasons_ids', 'Please Select')
list_referral_documents = get_list('referral_documents_ids')
list_case_plan_responsible = get_list('case_plan_responsible', 'Please Select')


YESNO_CHOICES = get_list('yesno_id')
care_option_list = get_list(
    'alternative_family_care_type_id', 'Please Select Care')

disability_degree = (('0', '0'), ('1', '1'), ('2', '2'),
                     ('3', '3'), ('4', '4'), )

YESNONA_choices = get_list('yesno_na')


class RadioCustomRenderer(RadioFieldRenderer):
    """Custom radio button renderer class."""

    def render(self):
        """Renderer override method."""
        return mark_safe(u'%s' % u'\n'.join(

            [u'%s' % force_unicode(w) for w in self]))


class AltCareForm(forms.Form):
    """AFC form."""

    has_consent = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'id': 'has_consent',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#has_consent_error"}))

    care_option = forms.ChoiceField(
        choices=care_option_list,
        initial='0',
        widget=forms.Select(
            attrs={'class': 'form-control', 'id': 'care_option',
                   'data-parsley-required': "true"}))

    case_date = forms.DateField(widget=forms.TextInput(
        attrs={'placeholder': _('Care initiation Date'),
               'class': 'form-control',
               'id': 'case_date',
               'data-parsley-required': "true"
               }))

    event_date = forms.DateField(widget=forms.TextInput(
        attrs={'placeholder': _('Date'),
               'class': 'form-control',
               'id': 'event_date',
               'data-parsley-required': "true"
               }))

    AFC_FM_Q1 = forms.MultipleChoiceField(
        choices=admission_reason_list,
        widget=forms.CheckboxSelectMultiple(
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#id_qf1A1"}))

    qf3A1_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'id': 'qf3A1_rdo',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf3A1_rdo_error"}))

    qf3A2_sdd = forms.ChoiceField(
        choices=consent_forms_list,
        initial='0',
        widget=forms.Select(
            attrs={'class': 'form-control', 'id': 'care_option',
                   'data-parsley-required': "true"}))

    qf3B1_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'id': 'qf3B1_rdo',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf3B1_rdo_error"}))


class AFCForm1A(forms.Form):
    """AFC Form 1A."""

    event_date = forms.DateField(widget=forms.TextInput(
        attrs={'placeholder': _('Date'),
               'class': 'form-control',
               'id': 'event_date',
               'data-parsley-required': "true"
               }))

    qf1A1_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'id': 'has_bcert',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1A1_rdo_error"}))

    qf1A2_txt = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': _(''),
               'class': 'form-control', 'id': 'qf1A2',
               'data-parsley-required': "false"}))

    qf1A3_txt = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': _(''),
               'class': 'form-control', 'id': 'qf1A3',
               'data-parsley-required': "false"}))

    qf1A4_txt = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': _(''),
               'class': 'form-control', 'id': 'qf1A4',
               'data-parsley-required': "false"}))

    qf1A5_txt = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': _(''),
               'class': 'form-control', 'id': 'qf1A5',
               'data-parsley-required': "false"}))

    qf1A6_txt = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': _(''),
               'class': 'form-control', 'id': 'qf1A6',
               'data-parsley-required': "false"}))

    qf1A7_txt = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': _(''),
               'class': 'form-control', 'id': 'qf1A7',
               'data-parsley-required': "false"}))

    qf1A8_txt = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': _(''),
               'class': 'form-control', 'id': 'qf1A8',
               'data-parsley-required': "false"}))

    qf1A10_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'id': 'has_disability',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1A2_rdo_error"}))

    qf1A11_sdd = forms.ChoiceField(
        choices=disability_list,
        initial='0',
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'id': 'disability_type'}))

    qf1A12_sdd = forms.ChoiceField(
        choices=severity_list,
        initial='0',
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'id': 'disability_severity'}))

    qf1A13_txt = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': _(''),
               'class': 'form-control', 'id': 'qf1A13',
               'data-parsley-required': "false"}))

    qf1A14_sdd = forms.ChoiceField(
        choices=list_other_adms,
        initial='0',
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'id': 'qf1A14_sdd'}))

    qf1A15_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1A15_rdo_error"}))

    qf1A16_txt = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': _(''),
               'class': 'form-control',
               'data-parsley-required': "false"}))

    qf1A17_txt = forms.DateField(widget=forms.TextInput(
        attrs={'placeholder': _(''),
               'class': 'form-control event_date',
               'data-parsley-required': "false"}))

    qf1A18_txt = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': _(''),
               'class': 'form-control',
               'data-parsley-required': "false"}))

    qf1A19_txt = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': _(''),
               'class': 'form-control',
               'data-parsley-required': "false"}))

    qf1A20_sdd = forms.ChoiceField(
        choices=list_other_vulnerability,
        widget=forms.Select(
            attrs={'class': 'form-control'}))

    qf1A21_txt = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': _(''),
               'class': 'form-control',
               'data-parsley-required': "false"}))

    qf1A21A_sdd = forms.ChoiceField(
        choices=list_relationship,
        widget=forms.Select(
            attrs={'class': 'form-control'}))

    qf1A22_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1A22_rdo_error"}))

    qf1A23_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1A23_rdo_error"}))

    qf1A24_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1A24_rdo_error"}))

    qf1A25_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'false',
                   'data-parsley-errors-container': "#qf1A25_rdo_error"}))

    qf1A25A_txt = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': _(''),
               'class': 'form-control',
               'data-parsley-required': "false"}))

    qf1A25B_txt = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': _(''),
               'class': 'form-control',
               'data-parsley-required': "false"}))

    qf1A26_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'false',
                   'data-parsley-errors-container': "#qf1A26_rdo_error"}))

    qf1A27_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'false',
                   'data-parsley-errors-container': "#qf1A27_rdo_error"}))

    qf1A27A_txt = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': _(''),
               'class': 'form-control',
               'data-parsley-required': "false"}))

    qf1A28_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1A28_rdo_error"}))


class AFCForm1B(forms.Form):
    """AFC Form 1B."""

    event_date = forms.DateField(widget=forms.TextInput(
        attrs={'placeholder': _('Date'),
               'class': 'form-control',
               'id': 'event_date',
               'data-parsley-required': "true"
               }))

    qf1B1B___txt = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    qf1B1A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1B1A_rdo_error"}))

    qf1B1B_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Details'),
               'class': 'form-control', 'rows': '2'}))

    qf1B2A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1B2A_rdo_error"}))

    qf1B2B_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Details'),
               'class': 'form-control', 'rows': '2'}))

    qf1B3A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1B3A_rdo_error"}))

    qf1B3B_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Details'),
               'class': 'form-control', 'rows': '2'}))

    qf1B4A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1B4A_rdo_error"}))

    qf1B4B_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Details'),
               'class': 'form-control', 'rows': '2'}))

    qf1B5A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1B5A_rdo_error"}))

    qf1B5B_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Details'),
               'class': 'form-control', 'rows': '2'}))

    qf1B6A_sdd = forms.ChoiceField(
        choices=immunization_list,
        initial='0',
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'data-parsley-required': "true",
                   'id': 'immunization'}))

    qf1B6B_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('If not fully, reason'),
               'class': 'form-control', 'rows': '2'}))

    qf1B7A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1B7A_rdo_error"}))

    qf1B7B_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Details'),
               'class': 'form-control', 'rows': '2'}))

    qf1B8_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Details'),
               'class': 'form-control', 'rows': '2'}))

    # School details

    qf1B9A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1B9A_rdo_error"}))

    qf1B9B_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('If yes, name'),
               'class': 'form-control', 'rows': '2'}))

    school_level = forms.ChoiceField(
        choices=school_level_list,
        initial='0',
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'data-parsley-required': "true",
                   'id': 'school_level'}))

    school_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Start typing then select',
               'id': 'school_name'}))

    school = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               'readonly': 'readonly',
               'id': 'school_id'}))

    admission_type = forms.ChoiceField(
        choices=admission_list,
        initial='0',
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'id': 'admission_type'}))

    school_class = forms.ChoiceField(
        choices=(),
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'id': 'school_class'}))

    qf1B10_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1B10_rdo_error"}))

    qf1B11_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1B11_rdo_error"}))

    qf1B12_rdo = forms.ChoiceField(
        choices=list_education_perf,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1B12_rdo_error"}))

    qf1B13_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Other details'),
               'class': 'form-control', 'rows': '2'}))

    # PSS

    qf1B14A_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Details'),
               'class': 'form-control', 'rows': '2'}))

    qf1B14B_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Details'),
               'class': 'form-control', 'rows': '2'}))

    qf1B14C_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Details'),
               'class': 'form-control', 'rows': '2'}))

    qf1B15_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Details'),
               'class': 'form-control', 'rows': '2'}))

    qf1B16_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Details'),
               'class': 'form-control', 'rows': '2'}))

    qf1B17_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Details'),
               'class': 'form-control', 'rows': '2'}))

    qf1B18A_rdo = forms.ChoiceField(
        choices=list_range_level,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1B18A_rdo_error"}))

    qf1B18B_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Describe'),
               'class': 'form-control', 'rows': '2'}))

    qf1B19A_rdo = forms.ChoiceField(
        choices=list_range_level,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1B19A_rdo_error"}))

    qf1B19B_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Describe'),
               'class': 'form-control', 'rows': '2'}))

    qf1B20 = forms.MultipleChoiceField(
        choices=list_child_exhibits,
        widget=forms.CheckboxSelectMultiple(
            attrs={'data-parsley-required': 'true'}))

    qf1B21_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Describe'),
               'class': 'form-control', 'rows': '2'}))

    qf1B22_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Describe'),
               'class': 'form-control', 'rows': '2'}))

    qf1B23_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Describe'),
               'class': 'form-control', 'rows': '2'}))

    qf1B24_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Describe'),
               'class': 'form-control', 'rows': '2'}))

    qf1B25_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Describe'),
               'class': 'form-control', 'rows': '2'}))

    qf1B26_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Describe'),
               'class': 'form-control', 'rows': '2'}))

    # Child perspective
    qf1B27A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1B27A_rdo_error"}))

    qf1B28A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1B28A_rdo_error"}))

    qf1B28B_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('If yes, explain'),
               'class': 'form-control', 'rows': '2'}))

    # Assessment conclusions

    qf1B30_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Details'),
               'class': 'form-control', 'rows': '2'}))

    qf1B31_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Details'),
               'class': 'form-control', 'rows': '2'}))

    qf1B32_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Details'),
               'class': 'form-control', 'rows': '2'}))

    qf1B33_txt = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': _('Details'),
               'class': 'form-control', 'rows': '2'}))


class AFCForm2A(forms.Form):
    """AFC Form 2A."""

    event_date = forms.DateField(
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': _('Date'),
                   'class': 'form-control',
                   'id': 'event_date',
                   'data-parsley-required': "true"
                   }))

    qf2A1_txt = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    qf2A2_sdd = forms.ChoiceField(
        choices=list_marriage_type,
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'data-parsley-required': "true"}))

    qf2A3_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _('Details'),
                   'class': 'form-control', 'rows': '2'}))

    qf2A4_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _('Details'),
                   'class': 'form-control', 'rows': '2'}))

    qf2A5_sdd = forms.ChoiceField(
        choices=list_items_count,
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'data-parsley-required': "true"}))

    qf2A6_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _('Details'),
                   'class': 'form-control', 'rows': '2'}))

    qf2A7_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _('Details'),
                   'class': 'form-control', 'rows': '2'}))

    qf2A8_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _('Details'),
                   'class': 'form-control', 'rows': '2'}))

    qf2A9_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _('Details'),
                   'class': 'form-control', 'rows': '2'}))

    qf2A10_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _('Details'),
                   'class': 'form-control', 'rows': '2'}))

    qf2A11_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _('Details'),
                   'class': 'form-control', 'rows': '2'}))

    qf2A12_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _('Details'),
                   'class': 'form-control', 'rows': '2'}))

    qf2A13_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _('Details'),
                   'class': 'form-control', 'rows': '2'}))

    qf2A14_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf2A14_rdo_error"}))

    qf2A15_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf2A15_rdo_error"}))

    qf2A16A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf2A16A_rdo_error"}))

    qf2A16B_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _('If yes, who, and what type'),
                   'class': 'form-control', 'rows': '2'}))

    qf2A17A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf2A17A_rdo_error"}))

    qf2A17B_txt = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'How many'}))

    qf2A18A = forms.MultipleChoiceField(
        required=False,
        choices=list_special_support,
        widget=forms.CheckboxSelectMultiple(
            attrs={'class': ''}))

    qf2A18B_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _('Other, details'),
                   'class': 'form-control', 'rows': '2'}))

    qf2A19A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf2A19A_rdo_error"}))

    qf2A19B_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _('Explain'),
                   'class': 'form-control', 'rows': '2'}))

    qf2A20 = forms.MultipleChoiceField(
        choices=list_community_services,
        required=False,
        widget=forms.CheckboxSelectMultiple(
            attrs={'class': ''}))

    qf2A21_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf2A21_rdo_error"}))

    qf2A22_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf2A22_rdo_error"}))

    qf2A23A_txt = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    qf2A23B_txt = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    qf2A23C_txt = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    qf2A23D_txt = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    qf2A24_sdd = forms.ChoiceField(
        choices=list_school_category,
        required=False,
        widget=forms.Select(
            attrs={'class': 'form-control'}))

    qf2A25A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf2A25A_rdo_error"}))

    qf2A25B_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("If no, describe child's unmet needs"),
                   'class': 'form-control', 'rows': '2'}))

    qf2A26A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf2A26A_rdo_error"}))

    qf2A26B_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'false',
                   'data-parsley-errors-container': "#qf2A26B_rdo_error"}))

    qf2A27_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf2A27_rdo_error"}))

    qf2A28_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Economic activity"),
                   'class': 'form-control', 'rows': '2'}))

    qf2A29_sdd = forms.ChoiceField(
        choices=list_employment_type,
        required=False,
        widget=forms.Select(
            attrs={'class': 'form-control'}))

    qf2A30_sdd = forms.ChoiceField(
        choices=list_income_range,
        required=False,
        widget=forms.Select(
            attrs={'class': 'form-control'}))

    qf2A31A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf2A31A_rdo_error"}))

    qf2A31B_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("If yes, by whom"),
                   'class': 'form-control', 'rows': '2'}))

    qf2A32_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Assets"),
                   'class': 'form-control', 'rows': '2'}))

    qf2A33A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf2A33A_rdo_error"}))

    qf2A33B_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Please describe"),
                   'class': 'form-control', 'rows': '2'}))

    qf2A34_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf2A34_rdo_error"}))

    qf2A35A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf2A35A_rdo_error"}))

    qf2A35B_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Please describe"),
                   'class': 'form-control', 'rows': '2'}))

    qf2A36_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf2A36_rdo_error"}))

    qf2A37_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Please describe"),
                   'class': 'form-control', 'rows': '2'}))

    qf2A38A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf2A38A_rdo_error"}))

    qf2A38B_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Details"),
                   'class': 'form-control', 'rows': '2'}))

    qf2A39A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf2A39A_rdo_error"}))

    qf2A39B_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Describe"),
                   'class': 'form-control', 'rows': '2'}))

    qf2A40A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf2A40A_rdo_error"}))

    qf2A40B_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Describe"),
                   'class': 'form-control', 'rows': '2'}))

    qf2A41A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf2A41A_rdo_error"}))

    qf2A41B_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Describe both +ve and -ve events"),
                   'class': 'form-control', 'rows': '2'}))

    qf2A42_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Describe"),
                   'class': 'form-control', 'rows': '2'}))

    qf2A43_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Describe"),
                   'class': 'form-control', 'rows': '2'}))

    qf2A44_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf2A44_rdo_error"}))

    qf2A45_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf2A45_rdo_error"}))

    qf2A46_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Describe"),
                   'class': 'form-control', 'rows': '2'}))

    qf2A47_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf2A47_rdo_error"}))

    qf2A48_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Describe"),
                   'class': 'form-control', 'rows': '2'}))

    qf2A49A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf2A49A_rdo_error"}))

    qf2A49B_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Describe"),
                   'class': 'form-control', 'rows': '2'}))

    qf2A50_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Describe"),
                   'class': 'form-control', 'rows': '2'}))

    qf2A51_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf2A51_rdo_error"}))

    qf2A52_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf2A52_rdo_error"}))

    qf2A53_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf2A53_rdo_error"}))

    qf2A54A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf2A54A_rdo_error"}))

    qf2A54B_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Examples"),
                   'class': 'form-control', 'rows': '2'}))

    qf2A55_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf2A55_rdo_error"}))

    qf2A56_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Describe"),
                   'class': 'form-control', 'rows': '2'}))

    qf2A57_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Describe"),
                   'class': 'form-control', 'rows': '2'}))

    qf2A58_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Describe"),
                   'class': 'form-control', 'rows': '2'}))

    qf2A59_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf2A59_rdo_error"}))

    qf2A60_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf2A60_rdo_error"}))

    qf2A61_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Describe"),
                   'class': 'form-control', 'rows': '3'}))

    qf2A62_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Describe"),
                   'class': 'form-control', 'rows': '3'}))

    qf2A63_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Describe"),
                   'class': 'form-control', 'rows': '3'}))

    qf2A64_sdd = forms.ChoiceField(
        choices=list_range_level,
        required=True,
        widget=forms.Select(
            attrs={'data-parsley-required': 'true',
                   'class': 'form-control'}))


class AFCForm4A(forms.Form):
    """AFC Form 4A."""

    event_date = forms.DateField(widget=forms.TextInput(
        attrs={'placeholder': _('Date'),
               'class': 'form-control',
               'id': 'event_date',
               'data-parsley-required': "true"
               }))

    qf4A1_sdd = forms.ChoiceField(
        choices=domain_list,
        initial='0',
        widget=forms.Select(
            attrs={'class': 'form-control', 'id': 'qf4A1',
                   'data-parsley-required': "true"}))

    qf4A2_sdd = forms.ChoiceField(
        choices=(),
        initial='0',
        widget=forms.Select(
            attrs={'class': 'form-control', 'id': 'qf4A2',
                   'data-parsley-required': "true"}))

    qf4A3_sdd = forms.ChoiceField(
        choices=(),
        initial='0',
        widget=forms.Select(
            attrs={'class': 'form-control', 'id': 'qf4A3',
                   'data-parsley-required': "true"}))

    qf4A4_sdd = forms.ChoiceField(
        choices=(),
        initial='0',
        widget=forms.Select(
            attrs={'class': 'form-control', 'id': 'qf4A4',
                   'data-parsley-required': "true"}))

    qf4A5_txt = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': _('Date'),
               'class': 'form-control event_date',
               'data-parsley-required': "true"
               }))

    qf4A6_sdd = forms.ChoiceField(
        choices=list_case_plan_responsible,
        initial='0',
        widget=forms.Select(
            attrs={'class': 'form-control', 'id': 'qf4A6',
                   'data-parsley-required': "true"}))

    qf4A7_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'id': 'qf4A1_rdo',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf4A7_rdo_error"}))

    qf4A8_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Explain"),
                   'class': 'form-control', 'rows': '2'}))

    qf4A9_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Explain"),
                   'class': 'form-control', 'rows': '2'}))


class AFCForm5A(forms.Form):
    """AFC Form 5A."""

    event_date = forms.DateField(widget=forms.TextInput(
        attrs={'placeholder': _('Date'),
               'class': 'form-control',
               'id': 'event_date',
               'data-parsley-required': "true"
               }))

    qf5A1 = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': _(''),
                   'class': 'form-control',
                   'data-parsley-required': "false"
                   }))

    qf5A2 = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': _(''),
                   'class': 'form-control',
                   'data-parsley-required': "false"
                   }))

    qf5A3_sdd = forms.ChoiceField(
        choices=(),
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control'}))

    qf5A3_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'id': 'qf5A1_rdo',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf5A3_rdo_error"}))

    qf5A4_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'id': 'qf5A1_rdo',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf5A4_rdo_error"}))

    qf5A5_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf5A5_rdo_error"}))

    qf5A6 = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control event_date',
                   'data-parsley-required': "false"
                   }))

    qf5A7 = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control event_date',
                   'data-parsley-required': "false"
                   }))

    qf5A8A = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    qf5A8B = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    qf5A8C = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    qf5A8D = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    qf5A9A = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    qf5A9B = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    qf5A9C = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    qf5A9D = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    qf5A10A = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    qf5A10B = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    qf5A10C = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    qf5A10D = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    qf5A11A = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    qf5A11B = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    qf5A11C = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    qf5A11D = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    qf5A12A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf5A12A_rdo_error"}))

    qf5A12B = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    qf5A12C = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    qf5A13_sdd = forms.ChoiceField(
        choices=care_option_list,
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control'}))

    qf5A14_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'class': 'form-control',
                   'data-parsley-errors-container': "#qf5A14_rdo_error"}))

    qf5A15A = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    qf5A15B_sdd = forms.ChoiceField(
        choices=list_sex_id,
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control'}))

    qf5A15C = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    qf5A16 = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    qf5A17 = forms.MultipleChoiceField(
        required=True,
        choices=admission_reason_list,
        widget=forms.CheckboxSelectMultiple(
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf5A17_error"}))


class AFCForm6A(forms.Form):
    """AFC Form 6A."""

    event_date = forms.DateField(widget=forms.TextInput(
        attrs={'placeholder': _('Date'),
               'class': 'form-control',
               'id': 'event_date',
               'data-parsley-required': "true"
               }))

    qf6A1_txt = forms.CharField(
        required=False,
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'min': '1'}))

    qf6A2_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Details"),
                   'class': 'form-control', 'rows': '2'}))

    qf6A3_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Details"),
                   'class': 'form-control', 'rows': '2'}))

    qf6A4_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Details"),
                   'class': 'form-control', 'rows': '2'}))

    qf6A5_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Details"),
                   'class': 'form-control', 'rows': '2'}))

    qf6A6_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Details"),
                   'class': 'form-control', 'rows': '2'}))

    qf6A7_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Details"),
                   'class': 'form-control', 'rows': '2'}))

    qf6A8_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Details"),
                   'class': 'form-control', 'rows': '2'}))

    qf6A9_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Details"),
                   'class': 'form-control', 'rows': '2'}))

    qf6A10_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Details"),
                   'class': 'form-control', 'rows': '2'}))

    qf6A11_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Details"),
                   'class': 'form-control', 'rows': '2'}))

    qf6A12_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Details"),
                   'class': 'form-control', 'rows': '2'}))

    qf6A13_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Details"),
                   'class': 'form-control', 'rows': '2'}))

    qf6A14_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Details"),
                   'class': 'form-control', 'rows': '2'}))
    qf6A15_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Details"),
                   'class': 'form-control', 'rows': '2'}))

    qf6A16_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Details"),
                   'class': 'form-control', 'rows': '2'}))

    qf6A17_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Details"),
                   'class': 'form-control', 'rows': '2'}))

    qf6A18_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Details"),
                   'class': 'form-control', 'rows': '2'}))

    qf6A19_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Details"),
                   'class': 'form-control', 'rows': '2'}))

    qf6A20_txt = forms.DateField(widget=forms.TextInput(
        attrs={'placeholder': _('Date'),
               'class': 'form-control event_date'
               }))


class AFCForm7A(forms.Form):
    """AFC Form 7A."""

    event_date = forms.DateField(widget=forms.TextInput(
        attrs={'placeholder': _('Date'),
               'class': 'form-control',
               'id': 'event_date',
               'data-parsley-required': "true"
               }))

    qf7A11_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A11_rdo_error"}))

    qf7A12_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A12_rdo_error"}))

    qf7A13_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A13_rdo_error"}))

    qf7A14_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A14_rdo_error"}))

    qf7A15_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A15_rdo_error"}))

    qf7A16_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A16_rdo_error"}))

    qf7A17_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A17_rdo_error"}))

    qf7A21_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A21_rdo_error"}))

    qf7A22_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A22_rdo_error"}))

    qf7A23_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A23_rdo_error"}))

    qf7A24_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A24_rdo_error"}))

    qf7A31_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A31_rdo_error"}))

    qf7A32_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A32_rdo_error"}))

    qf7A33_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A33_rdo_error"}))

    qf7A34_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A34_rdo_error"}))

    qf7A35_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A35_rdo_error"}))

    qf7A36_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A36_rdo_error"}))

    qf7A37_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A37_rdo_error"}))

    qf7A38_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A38_rdo_error"}))

    qf7A41_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A41_rdo_error"}))

    qf7A42_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A42_rdo_error"}))

    qf7A43_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A43_rdo_error"}))

    qf7A44_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A44_rdo_error"}))

    qf7A45_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A45_rdo_error"}))

    qf7A46_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A46_rdo_error"}))

    qf7A51_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A51_rdo_error"}))

    qf7A52_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A52_rdo_error"}))

    qf7A53_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A53_rdo_error"}))

    qf7A54_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A54_rdo_error"}))

    qf7A55_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A55_rdo_error"}))

    qf7A61_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A61_rdo_error"}))

    qf7A62_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A62_rdo_error"}))

    qf7A63_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A63_rdo_error"}))

    qf7A64_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A64_rdo_error"}))

    qf7A65_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A65_rdo_error"}))

    qf7A71_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A71_rdo_error"}))

    qf7A72_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A72_rdo_error"}))

    qf7A81_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A81_rdo_error"}))

    qf7A82_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A82_rdo_error"}))

    qf7A83_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A83_rdo_error"}))

    qf7A84_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A84_rdo_error"}))

    qf7A91_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A91_rdo_error"}))

    qf7A92_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A92_rdo_error"}))

    qf7A93_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A93_rdo_error"}))

    qf7A94_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A94_rdo_error"}))

    qf7A95_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A95_rdo_error"}))

    qf7A101_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A101_rdo_error"}))

    qf7A102_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A102_rdo_error"}))

    qf7A103_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A103_rdo_error"}))

    qf7A104_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A104_rdo_error"}))

    qf7A105_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A105_rdo_error"}))

    qf7A111_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A111_rdo_error"}))

    qf7A112_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A112_rdo_error"}))

    qf7A113_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A113_rdo_error"}))

    qf7A114_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A114_rdo_error"}))

    qf7A115_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A115_rdo_error"}))

    qf7A116_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A116_rdo_error"}))

    qf7A117_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A117_rdo_error"}))

    qf7A121_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A121_rdo_error"}))

    qf7A122_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A122_rdo_error"}))

    qf7A123_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A123_rdo_error"}))

    qf7A124_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A124_rdo_error"}))

    qf7A125_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A125_rdo_error"}))

    qf7A126_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A126_rdo_error"}))

    qf7A127_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf7A127_rdo_error"}))


class AFCForm8A(forms.Form):
    """AFC Form 8A."""

    event_date = forms.DateField(widget=forms.TextInput(
        attrs={'placeholder': _('Date'),
               'class': 'form-control',
               'id': 'event_date',
               'data-parsley-required': "true"
               }))

    qf8A11_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A11_rdo_error"}))

    qf8A12_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A12_rdo_error"}))

    qf8A13_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A13_rdo_error"}))

    qf8A14_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A14_rdo_error"}))

    qf8A15_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A15_rdo_error"}))

    qf8A16_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A16_rdo_error"}))

    qf8A17_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A17_rdo_error"}))

    qf8A21_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A21_rdo_error"}))

    qf8A22_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A22_rdo_error"}))

    qf8A23_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A23_rdo_error"}))

    qf8A24_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A24_rdo_error"}))

    qf8A31_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A31_rdo_error"}))

    qf8A32_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A32_rdo_error"}))

    qf8A33_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A33_rdo_error"}))

    qf8A34_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A34_rdo_error"}))

    qf8A35_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A35_rdo_error"}))

    qf8A36_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A36_rdo_error"}))

    qf8A41_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A41_rdo_error"}))

    qf8A42_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A42_rdo_error"}))

    qf8A43_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A43_rdo_error"}))

    qf8A44_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A44_rdo_error"}))

    qf8A45_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A45_rdo_error"}))

    qf8A51_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A51_rdo_error"}))

    qf8A52_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A52_rdo_error"}))

    qf8A53_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A53_rdo_error"}))

    qf8A54_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A54_rdo_error"}))

    qf8A55_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A55_rdo_error"}))

    qf8A61_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A61_rdo_error"}))

    qf8A62_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A62_rdo_error"}))

    qf8A63_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A63_rdo_error"}))

    qf8A64_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A64_rdo_error"}))

    qf8A71_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A71_rdo_error"}))

    qf8A81_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A81_rdo_error"}))

    qf8A82_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A82_rdo_error"}))

    qf8A91_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A91_rdo_error"}))

    qf8A92_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A92_rdo_error"}))

    qf8A101_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A101_rdo_error"}))

    qf8A102_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A102_rdo_error"}))

    qf8A111_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A111_rdo_error"}))

    qf8A112_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A112_rdo_error"}))

    qf8A113_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A113_rdo_error"}))

    qf8A114_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A114_rdo_error"}))

    qf8A121_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A121_rdo_error"}))

    qf8A122_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A122_rdo_error"}))

    qf8A123_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A123_rdo_error"}))

    qf8A124_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A124_rdo_error"}))

    qf8A125_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A125_rdo_error"}))

    qf8A126_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A126_rdo_error"}))

    qf8A127_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=False,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf8A127_rdo_error"}))


class AFCForm9A(forms.Form):
    """AFC Form 9A."""

    event_date = forms.DateField(widget=forms.TextInput(
        attrs={'placeholder': _('Date'),
               'class': 'form-control',
               'id': 'event_date',
               'data-parsley-required': "true"
               }))

    qf9AA_sdd = forms.ChoiceField(
        choices=list_closure_reasons,
        initial='0',
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'data-parsley-required': "true"}))

    qf9AB_rdo = forms.ChoiceField(
        choices=(('', 'Satisfied'), ('', 'Not Satisfied'),),
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf9A0B_rdo_error"}))

    qf9AC_rdo = forms.ChoiceField(
        choices=(('', 'Satisfied'), ('', 'Not Satisfied'),),
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf9A0C_rdo_error"}))

    qf9A1A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf9A1_rdo_error"}))

    qf9A1B_txt = forms.DateField(widget=forms.TextInput(
        attrs={'placeholder': _('Date'),
               'class': 'form-control event_date'
               }))

    qf9A2A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf9A1_rdo_error"}))

    qf9A2B_txt = forms.DateField(widget=forms.TextInput(
        attrs={'placeholder': _('Date'),
               'class': 'form-control event_date'
               }))

    qf9A3A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf9A1_rdo_error"}))

    qf9A3B_txt = forms.DateField(widget=forms.TextInput(
        attrs={'placeholder': _('Date'),
               'class': 'form-control event_date'
               }))

    qf9A4A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf9A1_rdo_error"}))

    qf9A4B_txt = forms.DateField(widget=forms.TextInput(
        attrs={'placeholder': _('Date'),
               'class': 'form-control event_date'
               }))

    qf9A5A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf9A1_rdo_error"}))

    qf9A5B_txt = forms.DateField(widget=forms.TextInput(
        attrs={'placeholder': _('Date'),
               'class': 'form-control event_date'
               }))
    qf9A6A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf9A1_rdo_error"}))

    qf9A6B_txt = forms.DateField(widget=forms.TextInput(
        attrs={'placeholder': _('Date'),
               'class': 'form-control event_date'
               }))


class AFCForm10A(forms.Form):
    """AFC Form 10A."""

    event_date = forms.DateField(
        widget=forms.TextInput(
            attrs={'placeholder': _('Date'),
                   'class': 'form-control',
                   'id': 'event_date',
                   'data-parsley-required': "true"
                   }))

    qf10A1A_sdd = forms.ChoiceField(
        choices=list_case_transfer_ids,
        initial='0',
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'data-parsley-required': "true"}))

    qf10A1B_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Describe"),
                   'class': 'form-control', 'rows': '3'}))

    qf10A2_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Describe"),
                   'class': 'form-control', 'rows': '3'}))

    qf10A3_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Describe"),
                   'class': 'form-control', 'rows': '3'}))

    qf10A4_txt = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    qf10A5_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Describe"),
                   'class': 'form-control', 'rows': '3'}))

    qf10A6_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Describe"),
                   'class': 'form-control', 'rows': '3'}))

    qf10A7_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Details"),
                   'class': 'form-control', 'rows': '3'}))

    qf10A8_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Details"),
                   'class': 'form-control', 'rows': '3'}))

    qf10A9_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Describe"),
                   'class': 'form-control', 'rows': '3'}))

    qf10A10_txt = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))


class AFCForm12A(forms.Form):
    """AFC Form 12A."""

    event_date = forms.DateField(widget=forms.TextInput(
        attrs={'placeholder': _('Date'),
               'class': 'form-control',
               'id': 'event_date',
               'data-parsley-required': "true"
               }))

    qf12A1_sdd = forms.ChoiceField(
        choices=list_referral_reasons,
        initial='0',
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'data-parsley-required': "true"}))

    qf12A2_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Details"),
                   'class': 'form-control', 'rows': '3'}))

    qf12A3_txt = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    qf12A4 = forms.MultipleChoiceField(
        choices=list_referral_documents,
        widget=forms.CheckboxSelectMultiple(
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#id_qf12A4"}))


class AFCForm14A(forms.Form):
    """AFC Form 14A."""

    event_date = forms.DateField(widget=forms.TextInput(
        attrs={'placeholder': _('Date'),
               'class': 'form-control',
               'id': 'event_date',
               'data-parsley-required': "true"
               }))

    qf14A1A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'id': 'qf9A1_rdo',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf14A1A_rdo_error"}))

    qf14A1B_rdo = forms.ChoiceField(
        choices=disability_degree,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf14A1B_rdo_error"}))

    qf14A1C_rdo = forms.ChoiceField(
        choices=disability_degree,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf14A1C_rdo_error"}))

    qf14A2A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'id': 'qf9A1_rdo',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf14A2A_rdo_error"}))

    qf14A2B_rdo = forms.ChoiceField(
        choices=disability_degree,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf14A2B_rdo_error"}))

    qf14A2C_rdo = forms.ChoiceField(
        choices=disability_degree,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'data-parsley-errors-container': "#qf14A2C_rdo_error"}))

    qf14A20_txt = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    qf14A3A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'id': 'qf14A3A_rdo',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf14A3A_rdo_error"}))

    qf14A4A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'id': 'qf14A4A_rdo',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf14A4A_rdo_error"}))

    qf14A5A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'id': 'qf14A5A_rdo',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf14A5A_rdo_error"}))

    qf14A6A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'id': 'qf14A6A_rdo',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf14A6A_rdo_error"}))

    qf14A7A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'id': 'qf14A7A_rdo',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf14A7A_rdo_error"}))

    qf14A8A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'id': 'qf14A8A_rdo',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf14A8A_rdo_error"}))

    qf14A9A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'id': 'qf14A9A_rdo',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf14A9A_rdo_error"}))

    qf14A10A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'id': 'qf14A10A_rdo',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf14A10A_rdo_error"}))

    qf14A11A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'id': 'qf14A11A_rdo',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf14A11A_rdo_error"}))

    qf14A12A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'id': 'qf14A12A_rdo',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf14A12A_rdo_error"}))

    qf14A13A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'id': 'qf14A13A_rdo',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf14A13A_rdo_error"}))

    qf14A14A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'id': 'qf14A14A_rdo',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf14A14A_rdo_error"}))

    qf14A15A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'id': 'qf14A15A_rdo',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf14A15A_rdo_error"}))

    qf14A16A_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'id': 'qf14A16A_rdo',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf14A16A_rdo_error"}))

    qf14A17A_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Details"),
                   'class': 'form-control', 'rows': '3'}))

    qf14A18A_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Details"),
                   'class': 'form-control', 'rows': '3'}))

    qf14A19_rdo = forms.ChoiceField(
        choices=(('', 'Please Select'), ),
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'id': 'qf14A19_rdo',
                   'data-parsley-errors-container': "#qf14A19_rdo_error"}))


class AFCForm15A(forms.Form):
    """AFC Form 15A."""

    event_date = forms.DateField(widget=forms.TextInput(
        attrs={'placeholder': _('Date'),
               'class': 'form-control',
               'id': 'event_date',
               'data-parsley-required': "true"
               }))

    qf15A1_rdo = forms.ChoiceField(
        choices=list_satisfied_level,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'id': 'qf15A1_rdo',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf15A1_rdo_error"}))

    qf15A3_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Details"),
                   'class': 'form-control', 'rows': '3'}))

    qf15A4_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Details"),
                   'class': 'form-control', 'rows': '3'}))


class AFCForm16A(forms.Form):
    """AFC Form 16A."""

    event_date = forms.DateField(widget=forms.TextInput(
        attrs={'placeholder': _('Date'),
               'class': 'form-control',
               'id': 'event_date',
               'data-parsley-required': "true"
               }))

    qf16A1_rdo = forms.ChoiceField(
        choices=list_feeling_level,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'id': 'qf16A1_rdo',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf16A1_rdo_error"}))

    qf16A2_rdo = forms.ChoiceField(
        choices=list_satisfied_level,
        required=True,
        widget=forms.RadioSelect(
            renderer=RadioCustomRenderer,
            attrs={'id': 'qf16A2_rdo',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf16A2_rdo_error"}))

    qf16A3_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Details"),
                   'class': 'form-control', 'rows': '3'}))

    qf16A4_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Details"),
                   'class': 'form-control', 'rows': '3'}))

    qf16A5_txt = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'placeholder': _("Details"),
                   'class': 'form-control', 'rows': '3'}))
