from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    args = '<domain> <name>'
    help = 'Creates a new user'

    def handle(self, *args, **options):
        # TODO get paramaters as flags
        # TODO check if organization exists
        # TODO check if domain isn't already associated
        pass
