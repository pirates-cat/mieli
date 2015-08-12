# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from identity.models import PID
from identity.api import pid
from mieli import helpers
from django import forms

def set_extra_fields(**kwargs):
    form = kwargs['form']
    fields = form.fields
    organization = helpers.get_current_organization()
    fields['first_name'] = forms.CharField(label=_('Nom'), max_length=30)
    fields['last_name'] = forms.CharField(label=_('Cognoms'), max_length=30)
    if organization.uid_field == 'pid':
        fields['pid_number'] = forms.RegexField(regex='^[A-Za-z]?[0-9]{7,8}[A-Za-z]$', max_length=10, label=_('DNI'), error_messages={'invalid': _(u'Només pot contenir lletres i números.')})
        fields['pid_upload'] = forms.FileField(label=_(u"Còpia del DNI (ambdues cares). Si no el tens a mà, fes-ne una fotografia. Si tens problemes per registrar-te, envia'ns les teves dades i el DNI (menys contrasenya) a partit@pirata.cat"))
    return kwargs

def clean_extra_fields(form, **kwargs):
    organization = helpers.get_current_organization()
    if organization.uid_field == 'pid': 
        if not 'pid_number' in form.cleaned_data:
            form.add_error('pid_number', _('DNI no vàlid'))
            return
        try:
            pid.get(organization, value)
            form.add_error('pid_number', _(u'DNI ja registrat.'))
        except PID.DoesNotExist:
            form.cleaned_data['pid_number'] = value
