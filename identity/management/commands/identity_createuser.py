from django.core.management.base import CommandError
from mieli.api import user, organization
from mieli.cli import MieliCommand
from optparse import make_option

class Command(MieliCommand):
    mandatory_options = ( 'organization', 'username', 'email' )
    option_list = BaseCommand.option_list + (
        make_option('--organization',
            dest='organization',
            help='Organization where created user will belong'),
        make_option('--username',
            dest='username',
            help='Username; it will have organization.tld appended'),
        make_option('--email',
            dest='email',
            help='E-mail used to identify and contact user'),
    )

    def invoke(self, *args, **options):
        domain = options.pop('organization')
        organization_ = organization.get(domain=domain)
        if organization_ == None:
            raise CommandError('unknown organization')
        options['username'] = "%s@%s" % (options['username'], organization_.domain)
        user.create(**options)
