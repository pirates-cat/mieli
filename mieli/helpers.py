from django.contrib.sites.models import Site
from django.conf import settings

def get_current_organization():
    sid = settings.SITE_ID
    site = Site.objects.get(pk=sid)
    return site.organization_set.get()
