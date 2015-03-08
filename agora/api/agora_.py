from agora.models import NexusAgora
from django.db import transaction
from django.conf import settings
from agora.api import link, user as agora_user

def get(**kwargs):
    try:
        n_agora = NexusAgora.objects.get(**kwargs)
    except NexusAgora.DoesNotExist:
        n_agora = None
    return n_agora

def get_by_nexus(nexus):
    if nexus == None:
        raise Exception("nexus required")
    options = { 'nexus': nexus }
    return get(**options)

@transaction.atomic
def create(nexus, **kwargs):
    n_agora = get_by_nexus(nexus)
    if n_agora:
        raise Exception("nexus '%s' already linked to agora '%s'" % (n_agora.nexus.name, n_agora.agora))
    kwargs = {}
    kwargs['pretty_name'] = '%s - %s' % (nexus.organization.domain, nexus.name)
    kwargs['short_description'] = nexus.name
    kwargs['is_vote_secret'] = True
    kwargs['__auth'] = True
    link_ = link.get(organization=nexus.organization)
    avr = link_.post('agora', **kwargs)
    options = {}
    options['agora'] = avr['name']
    options['agora_id'] = avr['id']
    options['nexus'] = nexus
    n_agora = NexusAgora(**options)
    n_agora.full_clean()
    n_agora.save()

def join(user, nexus, **kwargs):
    n_agora = get_by_nexus(nexus)
    if n_agora == None:
        raise Exception("nexus '%s' not linked" % (nexus.name))
    kwargs['action'] = 'add_membership'
    kwargs['username'] = agora_user.get_agora_username(user)
    kwargs['__auth'] = True
    n_agora.link.post('agora/%d/action' % n_agora.agora_id, **kwargs)
