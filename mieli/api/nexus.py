from identity.models import Nexus
from django.db import transaction
from django.conf import settings
from mieli import registry

def get(**kwargs):
    try:
        nexus = Nexus.objects.get(**kwargs)
    except Nexus.DoesNotExist:
        nexus = None
    return nexus

@transaction.atomic
def create(name, organization):
    if get(name=name, organization=organization):
        raise Exception("nexus '%s' already exists in '%s'" % (name, organization.domain))
    nexus = Nexus(name=name, organization=organization)
    nexus.full_clean()
    nexus.save()
    registry.invoke('nexus_create', nexus=nexus)
    return nexus

@transaction.atomic
def delete(**kwargs):
    nexus = get(**kwargs)
    if nexus == None:
        raise Exception('unknown nexus')
    registry.invoke('nexus_delete', nexus=nexus)
    nexus.delete()

def on_organization_creation(**kwargs):
    organization = kwargs['organization']
    main = get(name=settings.MAIN_NEXUS, organization=organization) # TODO name???
    if main:
        raise Exception("Main nexus '%s' already exists" % settings.MAIN_NEXUS)
    create(settings.MAIN_NEXUS, organization)
