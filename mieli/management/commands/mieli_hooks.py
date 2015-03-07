from django.core.management.base import CommandError
from mieli.cli import MieliCommand
from mieli.registry import __instance as registry

class Command(MieliCommand):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.register_option(
            '--event',
            dest='event',
            help='Event name',
            required=True)

    def print_hooks(self, event, level=1):
        if level == 1:
            print('-> %s' % event)
        hooks = registry[event]
        hooks_len = len(hooks)
        for ix, hook in enumerate(hooks):
            prefix = '%s|-' % (' ' * 3 * level)
            if ix == hooks_len - 1:
                prefix = prefix.replace('|-', '\\_')
            print('%s %s.%s' % (prefix, hook.__module__, hook.func_name))

    def invoke(self, *args, **options):
        # TODO Do Python code analysis to show a call tree
        event = options['event']
        if event not in registry:
            raise CommandError("event '%s' not registered" % event)
        self.print_hooks(event)
