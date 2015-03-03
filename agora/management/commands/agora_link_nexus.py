from django.core.management.base import CommandError
from mieli.api import organization, nexus
from mieli.cli import MieliCommand
from optparse import make_option

class Command(MieliCommand):
    mandatory_options = ( 'domain', 'nexus' )
    option_list = BaseCommand.option_list + (
        make_option('--organization',
            dest='domain',
            help='Organization\'s domain'),
        make_option('--nexus',
            dest='nexus',
            help='Nexus to link'),
    )

    def handle(self, *args, **options):
        organization_ = organization.get(domain=options['domain'])
        if organization_ == None:
            raise CommandError('unknown organization')
        nexus.create(nexus, organization_)
