from mieli.cli import MieliCommand
from optparse import make_option
from django.conf import settings
from agora.api import link

class Command(MieliCommand):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.register_option(
            '--organization',
            dest='org_domain',
            help='Organization\'s domain',
            required=True)
        self.register_option(
            '--url',
            dest='url',
            help='Agora Voting destination base URL',
            required=True)
        self.register_option(
            '--user',
            dest='user',
            help='Authentication user')
        self.register_option(
            '--token',
            dest='token',
            help='Authentication token',
            required=True)

    def invoke(self, *args, **options):
        link.create(**options)
