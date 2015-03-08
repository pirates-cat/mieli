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
            '--email',
            dest='email',
            help='E-mail used to identify and contact user',
            required=True)

    def invoke(self, *args, **options):
        domain = options.pop('organization')
        organization_ = organization.get(domain=domain)
        if organization_ == None:
            raise CommandError('unknown organization')
        options['username'] = "%s@%s" % (options['username'], organization_.domain)
        user.create(**options)
