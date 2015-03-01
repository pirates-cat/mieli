from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site

class Organization(models.Model):
    # Domains should be:
    # - 63: max length for DNS label https://en.wikipedia.org/wiki/Domain_Name_System#Domain_name_syntax
    # - 3: max number of DNS labels, as "subdomain.domain.tld"
    # Domain aliases must be handled on HTTP server layer. Nginx recommended.
    site = models.ForeignKey(Site)
    theme = models.CharField(max_length=32, default='default')
    # Is a meta-organization?
    meta = models.BooleanField(default=False)

class Nexus(models.Model):
    organization = models.ForeignKey(Organization)
    name = models.CharField(max_length=128)
    slug = models.SlugField()
    users = models.ManyToManyField(User)
