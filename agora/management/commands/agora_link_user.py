from django.core.management.base import CommandError
from identity.cli import IdentityUserCommand
from mieli.api import organization, nexus
from mieli.api import user as mieli_user
from agora.api import user, agora_
from django.conf import settings
from optparse import make_option

class Command(IdentityUserCommand):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.register_option(
            '--only-join',
            dest='only_join',
            action='store_true',
            default=False,
            help='Only join nexus agora')

    def invoke(self, *args, **options):
        if options['only_join']:
           nexus_ = nexus.get(name=settings.MAIN_NEXUS, organization=self.organization)
           agora_.join(self.user, nexus_)
        else:
           user.create(self.user)
