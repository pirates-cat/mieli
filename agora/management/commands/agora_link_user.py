from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from agora.api import user
from mieli.api import user as mieli_user
from mieli import cli

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--organization',
            dest='domain',
            help='Organization\'s domain'),
        make_option('--username',
            dest='username',
            help='User to sync. Organization will be appended'),
    )

    def handle(self, *args, **options):
        opts = cli.clean_options(options)
        for mandatory_arg in ('domain', 'username'):
            if mandatory_arg not in opts or opts[mandatory_arg] == None:
                raise CommandError('missing %s' % mandatory_arg)
        u = mieli_user.get(username='%s@%s' % (opts['username'], opts['domain']))
        if u == None:
            raise CommandError('unknown user')
        try:
            user.create(u)
        except Exception as e:
            raise CommandError(e)
