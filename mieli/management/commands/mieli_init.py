from django.core.management.base import BaseCommand, CommandError
from django.contrib.sites.models import Site

class Command(BaseCommand):
    def handle(self, *args, **options):
        sites = Site.objects.all()
        for site in sites:
            site.delete()
