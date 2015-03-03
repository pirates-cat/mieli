from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
import traceback
import copy

def clean_options(options):
    opts = copy.copy(options)
    del opts['pythonpath']
    del opts['settings']
    del opts['verbosity']
    del opts['traceback']
    del opts['no_color']
    return opts

class MieliCommand(BaseCommand):
    required_options = []
    option_list = BaseCommand.option_list 

    def register_option(self, *opts, **attrs):
        required = attrs.pop('required')
        option = make_option(*opts, **attrs)
        self.option_list += (option,)
        if required:
            self.required_options.append(option)

    def handle(self, *args, **options):
        opts = clean_options(options)
        for required_option in self.required_options:
            if required_option.dest not in opts or opts[required_option.dest] == None:
                raise CommandError('missing %s' % required_option.get_opt_string())
        try:
            self.invoke(*args, **opts)
        except Exception as e:
            if options['verbosity']:
                print traceback.format_exc()
            raise CommandError(e)

    def invoke(self, *args, **options):
        # Override this
        pass
