from mieli.api import nexus
from django.conf import settings

def create(nexus, **kwargs):
    if nx == None:
        raise Exception("unknown nexus '%s'" % name)
    lnk = link.get(organization=nexus.organization)
    if lnk == None:
        raise Exception("no Agora Voting link for organization '%s'" % org.domain)
    kwargs = {}
    kwargs['name'] = nexus.name
    lnk.post('agora/create???', **kwargs) # TODO
