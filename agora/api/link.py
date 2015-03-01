from mieli.api import organization
from agora.models import AVLink

def get(**kwargs):
    try:
        link = AVLink.objects.get(**kwargs)
    except AVLink.DoesNotExist:
        link = None
    return link

def create(org_domain, **kwargs):
    org = organization.get(domain=org_domain)
    if org == None:
        raise Exception('unknown organization')
    link = get(organization__site__domain=org_domain)
    if link:
        raise Exception("link for '%s' alredy established to '%s'" % (org_domain, link.url))
    kwargs['organization'] = org
    link = AVLink(**kwargs)
    link.full_clean()
    link.save()
    return link
