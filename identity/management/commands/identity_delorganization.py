from mieli.cli import MieliCommand
from mieli.api import organization

class Command(MieliCommand):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.register_option(
            '--organization',
            dest='domain',
            help='Organization to delete',
            required=True)

    def invoke(self, *args, **options):
        organization.delete(**options)
