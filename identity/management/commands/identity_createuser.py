from django.core.management.base import CommandError
from mieli.api import user, organization
from mieli.cli import MieliCommand
from optparse import make_option
from django.conf import settings
from mieli import registry

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
        self.register_option(
            '--firstname',
            dest='first_name',
            help='')
        self.register_option(
            '--lastname',
            dest='last_name',
            help='')
        self.register_option(
            '--pid',
            dest='pid',
            help='')
        registry.apply_filter('createuser_cli_options', command=self)

    def invoke(self, *args, **options):
        domain = options.pop('organization')
        organization_ = organization.get(domain=domain)
        if organization_ == None:
            raise CommandError('unknown organization')
        options['username'] = "%s@%s" % (options['username'], organization_.suffix)
        settings.SITE_ID._set(int(organization_.site.pk))
        user.create(**options)
