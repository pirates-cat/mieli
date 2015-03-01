from django.contrib.auth.models import User
from django.db import transaction
from mieli.api import organization
from mieli import registry
import random
import string

def get(**kwargs):
    try:
        user = User.objects.get(**kwargs)
    except User.DoesNotExist:
        user = None
    return user

def all(**kwargs):
    return User.objects.all(**kwargs)

@transaction.atomic
def create(username, email, send_invitation=False):
    kwargs = locals()
    if get(username=username):
        raise Exception("user '%s' already exists" % username)
    org = organization.get_by_username(username)
    query = { 'username__endswith': '@%s' % org.domain, org.uid_field: kwargs[org.uid_field] }
    if get(**query):
        raise Exception("unique identifier field '%s' with value '%s' already exists" % (org.uid_field, kwargs[org.uid_field]))
    kwargs['password'] = ''.join(random.choice(string.printable) for x in range(12))
    send_invitation = kwargs.pop('send_invitation')
    user = User(**kwargs)
    user.full_clean()
    user.save()
    registry.invoke('user_create', user=user)
    if send_invitation:
        # TODO send notification
        pass

@transaction.atomic
def delete(**kwargs):
    user = get(**kwargs)
    if user == None:
        raise Exception('unknown user')
    registry.invoke('user_delete', user=user)
    user.delete()

def delete_all(**kwargs):
    users = all(**kwargs)
    for user in users:
        user.delete()

def on_organization_deletion(**kwargs):
    org = kwargs['organization']
    delete_all(username__endswith='@%s' % org.domain)
