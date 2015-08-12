from django.core.management.base import CommandError
from mieli.cli import MieliCommand
from django.core import management
from mieli.api import user
import logging
import copy
import csv
import sys

class Command(MieliCommand):
    logger = logging.getLogger('main')

    def __init__(self):
        super(self.__class__, self).__init__()
        self.register_option(
            '--organization',
            dest='organization',
            help='Organization where load will be done',
            required=True)
        self.register_option(
            '--command',
            dest='command',
            help='Django\'s manage.py command to call for each row, using first row as arguments\' names',
            required=True)

    def invoke(self, *args, **options):
        reader = csv.reader(sys.stdin)
        try:
            header = reader.next()
            for row in reader:
                kwargs = copy.copy(options)
                for i in xrange(0, len(row)):
                    kwargs[header[i]] = row[i]
                try:
                    management.call_command(options['command'], **kwargs)
                except CommandError as e:
                    self.logger.exception(e)
        except csv.Error as e:
            sys.exit('line %d: %s' % (reader.line_num, e))
