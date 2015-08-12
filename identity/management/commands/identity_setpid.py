from django.core.management.base import CommandError
from identity.cli import IdentityUserCommand
from mieli.api import user, organization
from identity.api import pid

class Command(IdentityUserCommand):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.register_option(
            '--pid',
            dest='pid',
            help='Personal Identifier',
            required=True)

    def invoke(self, *args, **options):
        pid.set(self.user, self.organization, options['pid'])
