from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from mieli.api import organization, nexus
from mieli import cli

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--organization',
            dest='domain',
            help='Organization\'s domain'),
        make_option('--nexus',
            dest='nexus',
            help='Nexus to link'),
    )

    def handle(self, *args, **options):
        opts = cli.clean_options(options)
        for mandatory_arg in ('domain', 'nexus'):
            if mandatory_arg not in opts or opts[mandatory_arg] == None:
                raise CommandError('missing %s' % mandatory_arg)
        o = organization.get(domain=opts['domain'])
        if o == None:
            raise CommandError('unknown organization')
        try:
            nexus.create(nexus, o)
        except Exception as e:
            raise CommandError(e)
