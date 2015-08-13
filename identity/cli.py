from django.core.management.base import CommandError
from mieli.cli import MieliCommand
from mieli.api import user, organization

class IdentityUserCommand(MieliCommand):
    def __init__(self):
        super(IdentityUserCommand, self).__init__()
        self.register_option(
            '--organization',
            dest='organization',
            help='Organization where created user will belong',
            required=True)
        self.register_option(
            '--username',
            dest='username',
            help='Username; it will have organization.tld appended')
        self.register_option(
            '--email',
            dest='email',
            help='Email; if username is missing, it will be used to find it')

    def handle(self, *args, **options):
        self.organization = organization.get(domain=options['organization'])
        if self.organization == None:
            raise CommandError('unknown organization')
        if options['username']:
            username = "%s@%s" % (options['username'], self.organization.suffix)
            self.user = user.get(username=username)
            if self.user == None:
                raise CommandError('unknown user')
            self.email = self.user.email
            options['email'] = self.email
        elif options['email']:
            self.email = options['email']
            self.user = user.get_from_organization(self.organization, email=self.email)
            if self.user == None:
                raise CommandError('unknown user')
            options['username'] = self.user.username
        else:
            raise CommandError("no username nor email provided")
        super(IdentityUserCommand, self).handle(args, **options)
