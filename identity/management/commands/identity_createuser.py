from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from mieli.api import user, organization
from mieli import cli

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
        opts = cli.clean_options(options)
        for mandatory_option in ( 'organization', 'username', 'email'):
            if mandatory_option not in opts or opts[mandatory_option] == None:
                raise CommandError('missing %s' % mandatory_option)
        domain=opts.pop('organization')
        org = organization.get(domain=domain)
        if org == None:
            raise CommandError('unknown organization')
        opts['username'] = "%s@%s" % (opts['username'], org.domain)
        try:
            user.create(**opts)
        except Exception as e:
            raise CommandError(e)
