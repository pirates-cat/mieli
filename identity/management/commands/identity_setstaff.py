from django.core.management.base import CommandError
from mieli.api import user, organization
from mieli.cli import MieliCommand
from optparse import make_option

class Command(MieliCommand):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.register_option(
            '--organization',
            dest='organization',
            help='Organization where created user will belong',
            required=True)
        self.register_option(
            '--username',
            dest='username',
            help='Username; it will have organization.tld appended',
            required=True)
        self.register_option(
            '--disable',
            dest='disable',
            action='store_true',
            default=False,
            help='Disable staff status for given user (by default it\'s enabled)')

    def invoke(self, *args, **options):
        organization_ = organization.get(domain=options['organization'])
        if organization_ == None:
            raise CommandError('unknown organization')
        username = "%s@%s" % (options['username'], organization_.domain)
        user_ = user.get(username=username)
        if user_ == None:
            raise CommandError('unknown user')
        user_.is_staff = not options['disable']
        user_.save()
