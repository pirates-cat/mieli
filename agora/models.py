from django.db import models
from django.conf import settings
from identity.models import Organization, Nexus
import urllib2
import json

class OrganizationAgora(models.Model):
    organization = models.ForeignKey(Organization)
    url = models.URLField()

class AVLink(models.Model):
    agora = models.ForeignKey(OrganizationAgora)
    user = models.CharField(max_length=32, blank=False)
    token = models.CharField(max_length=64, blank=False)

    def post(self, _action, **kwargs):
        try:
            authorization = kwargs.pop('__auth')
        except KeyError:
            authorization = False
        endpoint = '%s/api/v1/%s/' % (self.url, _action)
        headers = { 'Accept': 'application/json, text/javascript', 'Content-Type': 'application/json; charset=utf-8' }
        if authorization:
            headers['Authorization'] = 'ApiKey %s:%s' % (self.user, self.token)
        req = urllib2.Request(endpoint, data=json.dumps(kwargs), headers=headers)
        try:
            f = urllib2.urlopen(req)
            r = f.read()
            f.close()
            if f.getcode() > 202:
                raise Exception("error %d on '%s': %s" % (f.getcode(), endpoint, r))
        except urllib2.HTTPError as e:
            r = e.fp.read()
        return json.loads(r)

    @property
    def url(self):
        return self.agora.url

class NexusAgora(models.Model):
    nexus = models.ForeignKey(Nexus)
    # 'name' field for model Agora at agora-ciudadana/agora_site/agora_core/models/agora.py
    agora = models.CharField(max_length=70, blank=False)
    agora_id = models.IntegerField()

    @property
    def link(self, api_user=settings.AGORA_ADMIN_USER):
        agoras = self.nexus.organization.organizationagora_set.all()
        if len(agoras) == 0:
            return None
        elif len(agoras) > 1:
            raise Exception("more than one agora defined for organization '%s'" % (self.nexus.organization.name))
        try:
            return agoras[0].avlink_set.get(user=api_user)
        except AVLink.DoesNotExist:
            return None
