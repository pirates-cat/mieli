from mieli import registry
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.sites.models import Site, _simple_domain_name_validator
import slugify
import time
import os

class Organization(models.Model):
    # Domains should be:
    # - 63: max length for DNS label https://en.wikipedia.org/wiki/Domain_Name_System#Domain_name_syntax
    # - 3: max number of DNS labels, as "subdomain.domain.tld"
    # Domain aliases must be handled on HTTP server layer. Nginx recommended.
    site = models.ForeignKey(Site)
    # Three letter alias (only useful when user@domain is bigger than 30)
    alias = models.CharField(max_length=3, blank=True)
    theme = models.CharField(max_length=32, default='default')
    # Is a meta-organization?
    meta = models.BooleanField(default=False)
    # UID field: User's field used as unique identifier (30 chars due max. Oracle column name's length)
    uid_field = models.CharField(max_length=30, default='email')
    contact = models.EmailField(blank=True)
    email_host = models.CharField(max_length=100, validators=[_simple_domain_name_validator], blank=True)
    email_port = models.IntegerField(default=587)
    email_host_user = models.CharField(max_length=30, blank=True)
    email_host_password = models.CharField(max_length=100, blank=True)
    email_use_tls = models.BooleanField(default=True)
    email_use_ssl = models.BooleanField(default=False)
    web = models.URLField(blank=True)

    @property
    def domain(self):
        return self.site.domain

    @property
    def suffix(self):
        if self.alias:
            return self.alias
        return self.domain

    @property
    def name(self):
        return self.site.name

    @property
    def main_nexus(self):
        try:
            return Nexus.objects.get(organization=self, slug=slugify.slugify(settings.MAIN_NEXUS, to_lower=True))
        except Nexus.DoesNotExist:
            return None

    def __unicode__(self):
       return self.name

class Nexus(models.Model):
    organization = models.ForeignKey(Organization)
    name = models.CharField(max_length=128)
    slug = models.SlugField()
    users = models.ManyToManyField(User)

    def join(self, user):
        self.users.add(user)
        registry.signal('user_join', user=user, nexus=self)

    def __unicode__(self):
       return u'%s - %s' % (self.organization.domain, self.slug)


def get_upload_path(instance, file_):
    file_name, file_ext = os.path.splitext(file_)
    return os.path.join('pids', instance.organization.domain, time.strftime('%Y/%m/%d'), '%s%s' % (slugify.slugify(file_name), file_ext))

# Personal Identification Document
class PID(models.Model):
    user = models.ForeignKey(User)
    organization = models.ForeignKey(Organization)
    value = models.CharField(max_length=10)
    document = models.FileField(upload_to=get_upload_path)
