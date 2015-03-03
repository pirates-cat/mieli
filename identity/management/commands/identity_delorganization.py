from mieli.cli import MieliCommand
from mieli.api import organization

class Command(MieliCommand):
    option_list = BaseCommand.option_list + (
        make_option('--domain',
            dest='domain',
            help='Organization\'s domain',
            mandatory=True),
    )

    def invoke(self, *args, **options):
        organization.delete(**options)
