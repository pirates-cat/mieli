from django.core.management.base import CommandError
from identity.cli import IdentityUserCommand
from mieli.api import user, organization
from optparse import make_option
from geo.api import location

class Command(IdentityUserCommand):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.register_option(
            '--name',
            dest='name',
            help='Location name',
            required=True)
        self.register_option(
            '--country',
            dest='country',
            help='Location country',
            required=True)

    def invoke(self, *args, **options):
        name = options['name']
        result = location.find(name, options['country'])
        if len(result) == 0:
            raise CommandError("no location find by name '%s' for '%s'" % (name, username))
        location.save(self.user, result[0])
