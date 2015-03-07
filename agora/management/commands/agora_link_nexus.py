from django.core.management.base import CommandError
from mieli.api import organization, nexus
from mieli.cli import MieliCommand
from optparse import make_option
import slugify

class Command(MieliCommand):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.register_option(
            '--organization',
            dest='domain',
            help='Nexus organization',
            required=True)
        self.register_option(
            '--nexus',
            dest='nexus',
            help='Nexus to link',
            required=True)

    def invoke(self, *args, **options):
        domain = options['domain']
        name = slugify.slugify(options['nexus'])
        organization_ = organization.get(domain=domain)
        if organization_ == None:
            raise CommandError("unknown organization '%s'" % domain)
        nexus_ = nexus.get(slug=nexus, organization=organization_)
        if nexus_ == None:
            raise CommandError("unknown nexus '%s'" % name)
        agora.create(nexus_)
