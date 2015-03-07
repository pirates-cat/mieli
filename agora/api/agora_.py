from django.conf import settings
from agora.api import link
import slugify

def create(nexus, **kwargs):
    if nexus == None:
        raise Exception("nexus required")
    lnk = link.get(organization=nexus.organization)
    if lnk == None:
        raise Exception("no Agora Voting link for organization '%s'" % nexus.organization.domain)
    kwargs = {}
    kwargs['pretty_name'] = '%s-%s' % (slugify.slugify(nexus.organization), nexus.slug)
    kwargs['short_description'] = nexus.name
    kwargs['is_vote_secret'] = True
    lnk.post('agora', **kwargs)
