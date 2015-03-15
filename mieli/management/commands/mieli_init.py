from mieli.cli import MieliCommand
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group

class Command(MieliCommand):
    def invoke(self, *args, **options):
        sites = Site.objects.all()
        for site in sites:
            site.delete()
        Group.objects.create(name='superusers')
