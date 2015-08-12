# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from geo.api import location
from django import forms
import re

def __admin2_sanitizer(admin2):
    admin2.name = admin2.name.split(' ')[-1]
    return admin2

def build_administrative_2_divisions(admin1_code):
    admin2_divisions = map(__admin2_sanitizer, location.load_administrative_2_divisions(admin1_code.countrycode, admin1_code.admin1_code))
    return [('', '')] + sorted(map(lambda x: (x.geonameid, x.name[0].upper() + x.name[1:]), admin2_divisions), key=lambda x: x[1])

def build_places(admin1_code):
    places = location.load_places(admin1_code.countrycode, admin1_code.admin1_code)
    return [('', '')] + sorted(map(lambda x: (x.geonameid, x.name[0].upper() + x.name[1:]), places), key=lambda x: x[1])

def set_extra_fields(**kwargs):
    form = kwargs['form']
    form.initial['administrative_division'] = ''
    form.initial['place'] = ''
    fields = form.fields
    catalonia = filter(lambda x: x.name == 'Catalonia', location.load_administrative_divisions('ES'))[0]
    fields['administrative_division'] = forms.ChoiceField(label=_('Prov&iacute;ncia'), choices=build_administrative_2_divisions(catalonia))
    fields['place'] = forms.ChoiceField(label=_('Municipi'), choices=build_places(catalonia))
    return kwargs

def clean_extra_fields(form, **kwargs):
    if not 'administrative_division' in form.cleaned_data:
        form.add_error('administrative_division', _('Indica una prov&iacute;ncia'))
        return
    if not 'place' in form.cleaned_data:
        form.add_error('place', _('Indica un municipi'))
        return
    if form.cleaned_data['administrative_division'] == '':
        form.add_error('administrative_division', _('Indica una prov&iacute;ncia'))
        return
    if form.cleaned_data['place'] == '':
        form.add_error('place', _('Indica un municipi'))
        return

def on_user_creation(user, **kwargs):
    if 'location' in kwargs:
        if kwargs['location'] == None:
            if 'place' in kwargs:
                if kwargs['place'] == '':
                    raise Exception('Place missing')
                kwargs['location'] = kwargs['place']
            else:
                return
    else:
        if not 'place' in kwargs:
            return
        kwargs['location'] = kwargs['place']
    place = Geoname.objects.get(geonameid=kwargs['location'])
    administrative_division_id = None
    if 'administrative_division' in kwargs:
        administrative_division_id = kwargs['administrative_division']
    location.save(user, place, administrative_division_id)
