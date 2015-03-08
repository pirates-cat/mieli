from mieli.cli import MieliCommand
from mieli.api import organization
from optparse import make_option
from mieli import registry

class Command(MieliCommand):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.register_option(
            '--domain',
            dest='domain',
            help='Organization\'s domain',
            required=True)
        self.register_option(
            '--name',
            dest='name',
            help='Public name for organization',
            required=True)
        registry.apply_filter('createorganization_cli_options', command=self)

    def invoke(self, *args, **options):
        organization.create(**options)
