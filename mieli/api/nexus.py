from identity.models import Nexus
from django.db import transaction
from django.conf import settings
from mieli import registry
import slugify

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
    nexus = Nexus(name=name, organization=organization, slug=slugify.slugify(name, to_lower=True))
    nexus.full_clean()
    nexus.save()
    registry.signal('nexus_create', nexus=nexus)
    return nexus

@transaction.atomic
def delete(**kwargs):
    nexus = get(**kwargs)
    if nexus == None:
        raise Exception('unknown nexus')
    registry.signal('nexus_delete', nexus=nexus)
    nexus.delete()

def on_organization_creation(**kwargs):
    registry.signal('organization_init', **kwargs)
    create(settings.MAIN_NEXUS, kwargs['organization'])

def auto_join(user, **kwargs):
    nexus = get(slug=slugify.slugify(settings.MAIN_NEXUS, to_lower=True))
    if nexus == None:
        raise Exception("main nexus '%s' doesn't exist" % settings.MAIN_NEXUS)
    nexus.join(user)
