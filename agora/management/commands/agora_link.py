from mieli.cli import MieliCommand
from optparse import make_option
from agora.api import link

class Command(MieliCommand):
    mandatory_options = ( 'org_domain', 'url', 'user', 'token' )
    option_list = BaseCommand.option_list + (
        make_option('--organization',
            dest='org_domain',
            help='Organization\'s domain'),
        make_option('--url',
            dest='url',
            help='Agora Voting destination base URL'),
        make_option('--user',
            dest='user',
            help='Authentication user'),
        make_option('--token',
            dest='token',
            help='Authentication token'),
    )

    def invoke(self, *args, **options):
        link.create(**options)
