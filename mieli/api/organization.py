from identity.models import Organization
from django.contrib.sites.models import Site
from django.db import transaction
from mieli import registry
import random
import string
import copy

def setup_query(kwargs):
    query = copy.copy(kwargs)
    for key in kwargs.iterkeys():
        if key == 'domain' or key == 'name':
            value = query.pop(key)
            query['site__%s' % key] = value
    return query

def get(**kwargs):
    query = setup_query(kwargs)
    try:
        organization = Organization.objects.get(**query)
    except Organization.DoesNotExist:
        organization = None
    return organization

def get_by_username(username):
    if not '@' in username:
        raise Exception("invalid username '%s', expected username@organization" % username)
    domain = username.split('@')[1]
    query = { 'domain': domain }
    return get(**query)

@transaction.atomic
def create(domain, name, **kwargs):
    if get(domain=domain):
        raise Exception('domain %s is already in use' % domain)
    site = Site(domain=domain, name=name)
    site.full_clean()
    site.save()
    organization = Organization(site=site)
    organization.full_clean()
    organization.save()
    registry.signal('organization_create', organization=organization, **kwargs)
    return organization

@transaction.atomic
def delete(**kwargs):
    organization = get(**kwargs)
    if organization == None:
        raise Exception('unknown organization')
    registry.signal('organization_delete', organization=organization, **kwargs)
    organization.site.delete()
