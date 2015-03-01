from identity.models import Organization
from django.contrib.sites.models import Site
import random
import string
import copy

def setup_filter(args):
    cargs = copy.copy(args)
    for key in args.iterkeys():
        if key == 'domain' or key == 'name':
            value = cargs.pop(key)
            cargs['site__%s' % key] = value
    return cargs

def get(**args):
    query = setup_filter(args)
    try:
        organization = Organization.objects.get(**query)
    except Organization.DoesNotExist:
        organization = None
    return organization

def create(domain, name):
    site = Site(domain=domain, name=name)
    site.full_clean()
    site.save()
    organization = Organization(site=site)
    organization.full_clean()
    organization.save()

def delete(**args):
    query = setup_filter(args)
    organization = get(**query)
    organization.site.delete()
