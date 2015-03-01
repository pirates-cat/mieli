from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from agora.api import link
from mieli import cli

class Command(BaseCommand):
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

    def handle(self, *args, **options):
        opts = cli.clean_options(options)
        for mandatory_arg in ('org_domain', 'url', 'user', 'token'):
            if mandatory_arg not in opts or opts[mandatory_arg] == None:
                raise CommandError('missing %s' % mandatory_arg)
        try:
            link.create(**opts)
        except Exception as e:
            raise CommandError(e)
