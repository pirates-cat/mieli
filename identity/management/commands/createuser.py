from django.core.management.base import BaseCommand
from optparse import make_option
from mieli.api import user, organization

class Command(BaseCommand):
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

    def handle(self, *args, **options):
        # TODO check if organization exists
        # TODO check if user is free
        # TODO check if email isn't already associated
        username = "%s@%s" % (options['username'], organization)
        user.create(username, options['email'])
