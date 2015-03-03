from mieli.cli import MieliCommand
from mieli import registry

class Command(MieliCommand):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.register_option(
            '--event',
            dest='event',
            help='Event name',
            required=True)

    def invoke(self, *args, **options):
        # TODO improve with tree output
        pass
