from identity.models import Organization
import random
import string

def get(**args):
    try:
        organization = Organization.objects.get(**args)
    except Organization.DoesNotExist:
        organization = None
    return organization

def create(domain, name):
    organization = Organization.objects.create(domain=domain, name=name)
    organization.full_clean()
    organization.save()
