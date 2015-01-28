from django.db import models
from django.contrib.auth.models import User

class Organization(models.Model):
    name = models.CharField(max_length=128)
    # Magic numbers:
    # - 63: max length for DNS label https://en.wikipedia.org/wiki/Domain_Name_System#Domain_name_syntax
    # - 3: max number of DNS labels, as "subdomain.domain.tld"
    # Domain aliases must be handled on HTTP server layer. Nginx recommended.
    domain = models.CharField(max_length=63*3)
    # Is a meta-organization?
    meta = models.BooleanField()

class Nexus(models.Model):
    organization = models.ForeignKey(Organization)
    name = models.CharField(max_length=128)
    users = models.ManyToManyField(User)
