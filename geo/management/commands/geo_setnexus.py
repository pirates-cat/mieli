from django.core.management.base import CommandError
from identity.cli import IdentityUserCommand
from mieli.api import nexus, user
from geo.api import location

class Command(IdentityUserCommand):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.register_option(
            '--admindiv',
            dest='admindiv',
            help='Administrative division\'s name (second level)',
            required=True)
        self.register_option(
            '--nexus',
            dest='nexus',
            help='Nexus\' name',
            required=True)

    def invoke(self, *args, **options):
        name = options['nexus']
        nexus_ = nexus.get(name=name, organization=self.organization)
        if nexus_ == None:
            raise CommandError("nexus '%s' not found" % name)
        admin1 = filter(lambda x: x.name == 'Catalonia', location.load_administrative_divisions('ES'))[0]
        admin2 = location.load_administrative_2_divisions(admin1.countrycode, admin1.admin1_code).get(name=options['admindiv'])
        if admin2 == None:
            raise CommandError("administrative division '%s' not found" % options['admindiv'])
        if self.user.location_set.get().admin2 == admin2:
            if nexus_ not in self.user.nexus_set.all():
                nexus_.join(self.user)
