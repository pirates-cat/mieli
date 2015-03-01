from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from mieli.api import organization
from mieli import cli

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--domain',
            dest='domain',
            help='Organization\'s domain'),
    )

    def handle(self, *args, **options):
        opts = cli.clean_options(options)
        if 'domain' not in opts or opts['domain'] == None:
            raise CommandError('missing domain')
        try:
            organization.delete(**opts)
        except Exception as e:
            raise CommandError(e)
