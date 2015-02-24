from django.contrib.auth.models import User
import random
import string

def create(username, email, notification=False):
    # TODO send notification
    password = ''.join(random.choice(string.printable) for x in range(12))
    user = User.objects.create_user(username, email, password)
    user.full_clean()
    user.save()
