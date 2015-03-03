from mieli.cli import MieliCommand
from mieli.api import organization
from optparse import make_option

class Command(MieliCommand):
    mandatory_options = ( 'domain' )
    option_list = BaseCommand.option_list + (
        make_option('--domain',
            dest='domain',
            help='Organization\'s domain'),
        make_option('--name',
            dest='name',
            help='Public name for organization'),
    )

    def invoke(self, *args, **options):
        organization.create(**options)
