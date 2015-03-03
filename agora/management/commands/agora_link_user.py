from django.core.management.base import CommandError
from mieli.api import user as mieli_user
from mieli.cli import MieliCommand
from optparse import make_option
from agora.api import user

class Command(MieliCommand):
    mandatory_options = ( 'domain', 'username' )
    option_list = BaseCommand.option_list + (
        make_option('--organization',
            dest='domain',
            help='Organization\'s domain'),
        make_option('--username',
            dest='username',
            help='User to sync. Organization will be appended'),
    )

    def invoke(self, *args, **options):
        user_ = mieli_user.get(username='%s@%s' % (options['username'], options['domain']))
        if user_ == None:
            raise CommandError('unknown user')
        user.create(user_)
