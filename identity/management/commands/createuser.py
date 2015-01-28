from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    args = '<username> <organization.tld> <email>'
    help = 'Creates a new user'

    def handle(self, *args, **options):
        # TODO get paramaters as flags
        # TODO check if organization exists
        # TODO check if user is free
        # TODO check if email isn't already associated
        user = User.objects.create_user(username, email, 'randompassword')
        user.save()
