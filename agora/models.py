from django.db import models
from identity.models import Organization
import urllib2
import json

class AVLink(models.Model):
    organization = models.ForeignKey(Organization)
    url = models.URLField()
    user = models.CharField(max_length=32)
    token = models.CharField(max_length=64)

    def post(self, action, **kwargs):
        endpoint = '%s/api/v1/%s/' % (self.url, action)
        headers = { 'Accept': 'application/json, text/javascript', 'Content-Type': 'application/json; charset=utf-8' }
        req = urllib2.Request(endpoint, data=json.dumps(kwargs), headers=headers)
        try:
            f = urllib2.urlopen(req)
            r = f.read()
            f.close()
            if f.getcode() != 200:
                raise Exception("error %d on '%s'" % (f.getcode(), endpoint))
        except urllib2.HTTPError as e:
            raise Exception(e.read())
