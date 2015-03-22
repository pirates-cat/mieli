from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site
from django.conf import settings
from identity.models import PID
from django import forms
import re

def get_current_organization():
    sid = settings.SITE_ID
    site = Site.objects.get(pk=sid)
    return site.organization_set.get()

def set_extra_fields(form, **kwargs):
    fields = form.fields
    organization = get_current_organization()
    fields['first_name'] = forms.CharField(max_length=30)
    fields['last_name'] = forms.CharField(max_length=30)
    if organization.uid_field == 'pid':
        fields['pid_number'] = forms.RegexField(regex='^[A-Z]?[0-9]{7,8}[A-Z]$', max_length=10, label=_('PID'), error_messages={'invalid': _('This value may contain only letters and numbers.')})
        fields['pid_upload'] = forms.FileField()

def clean_extra_fields(form, **kwargs):
    organization = get_current_organization()
    if organization.uid_field == 'pid':   
        value = re.sub('[^A-Z0-9]', '', form.cleaned_data['pid_number'].upper())
        try:
            PID.objects.get(organization=organization, value=value)
            form.add_error('pid_number', _('Personal Identification Document already registered.'))
        except PID.DoesNotExist:
            form.cleaned_data['pid_number'] = value
