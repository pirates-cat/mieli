from mieli.cli import MieliCommand
from django.contrib.auth.models import User

class Command(MieliCommand):
    #args = '<slug> <name> <organization.tld>'

    def invoke(self, *args, **options):
        # TODO check if organization exists
        # TODO check if slug is free
        pass
