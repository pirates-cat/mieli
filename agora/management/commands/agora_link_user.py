from django.core.management.base import CommandError
from mieli.api import organization, nexus
from mieli.api import user as mieli_user
from mieli.cli import MieliCommand
from agora.api import user, agora_
from django.conf import settings
from optparse import make_option

class Command(MieliCommand):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.register_option(
            '--organization',
            dest='domain',
            help='Nexus organization',
            required=True)
        self.register_option(
            '--username',
            dest='username',
            help='User to sync. Organization will be appended',
            required=True)
        self.register_option(
            '--only-join',
            dest='only_join',
            action='store_true',
            default=False,
            help='Only join nexus agora')

    def invoke(self, *args, **options):
        user_ = mieli_user.get(username='%s@%s' % (options['username'], options['domain']))
        if user_ == None:
            raise CommandError('unknown user')
        if options['only_join']:
           organization_ = organization.get_by_username(user_.username)
           nexus_ = nexus.get(name=settings.MAIN_NEXUS, organization=organization_)
           agora_.join(user_, nexus_)
        else:
           user.create(user_)
