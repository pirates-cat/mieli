from mieli.cli import MieliCommand
from mieli.api import nexus, organization
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
            '--name',
            dest='name',
            help='Nexus name',
            required=True)

    def invoke(self, *args, **options):
        domain = options.pop('domain')
        organization_ = organization.get(domain=domain)
        if organization_ == None:
            raise CommandError('unknown organization')
        options['organization'] = organization_
        nexus.create(**options)
