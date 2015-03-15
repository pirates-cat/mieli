from mieli.api import organization as mieli_organization
from agora.models import AVLink, OrganizationAgora
from django.db import transaction
from django.conf import settings
import copy

def setup_query(kwargs):
    query = copy.copy(kwargs)
    for key in kwargs.iterkeys():
        if key == 'organization' or key == 'url' or key.startswith('organization_'):
            value = query.pop(key)
            query['agora__%s' % key] = value
    return query

def get(**kwargs):
    query = setup_query(kwargs)
    try:
        link = AVLink.objects.get(**query)
    except AVLink.DoesNotExist:
        link = None
    return link

@transaction.atomic
def create(org_domain, **kwargs):
    org = mieli_organization.get(domain=org_domain)
    if org == None:
        raise Exception("unknown organization '%s'" % org_domain)
    try:
        link = OrganizationAgora.objects.get(organization=org)
    except OrganizationAgora.DoesNotExist:
        link = None
    if link == None:
        if 'url' in kwargs:
            link = OrganizationAgora(organization=org, url=kwargs.pop('url'))
            link.save()
        else:
            raise Exception("you tried to link organization '%s' for first time without providing an url" % org.name)
    if not 'user' in kwargs or kwargs['user'] == None:
        kwargs['user'] = settings.AGORA_ADMIN_USER
    kwargs['agora'] = link
    avlink = AVLink(**kwargs)
    avlink.full_clean()
    avlink.save()
    return avlink

@transaction.atomic
def delete(org_domain, **kwargs):
    org = mieli_organization.get(domain=org_domain)
    if org == None:
        raise Exception("unknown organization '%s'" % org_domain)
    try:
        link = OrganizationAgora.objects.get(organization=org)
        link.delete()
    except OrganizationAgora.DoesNotExist:
        pass

def on_organization_creation(organization, **kwargs):
    create(organization.domain, **kwargs)
