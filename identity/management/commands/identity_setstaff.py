from django.core.management.base import CommandError
from identity.cli import IdentityUserCommand
from mieli.api import user, organization
from optparse import make_option

class Command(IdentityUserCommand):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.register_option(
            '--organization',
            dest='organization',
            help='Organization where created user will belong',
            required=True)
        self.register_option(
            '--disable',
            dest='disable',
            action='store_true',
            default=False,
            help='Disable staff status for given user (by default it\'s enabled)')

    def invoke(self, *args, **options):
        self.user.is_staff = not options['disable']
        self.user.save()
