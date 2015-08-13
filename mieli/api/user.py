# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db import transaction
from mieli.api import organization
from identity.api import pid
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

def get_from_organization(org, **kwargs):
    return get(username__endswith='@%s' % org.suffix, **kwargs)

def from_organization(org, **kwargs):
    return User.objects.filter(username__endswith='@%s' % org.suffix, **kwargs)

@transaction.atomic
def create(username, email, send_invitation=True, **qwargs):
    kwargs = locals()
    if get(username=username):
        raise Exception("user '%s' already exists" % username)
    org = organization.get_by_username(username)
    query = { 'username__endswith': '@%s' % org.suffix }
    if org.uid_field == 'pid':
        query['pid__value'] = qwargs[org.uid_field]
    if get(**query):
        raise Exception("unique identifier field '%s' with value '%s' already exists" % (org.uid_field, kwargs[org.uid_field]))
    raw_password = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(10))
    send_invitation = kwargs.pop('send_invitation')
    _ = kwargs.pop('qwargs')
    user = User(**kwargs)
    user.set_password(raw_password)
    user.full_clean()
    user.save()
    if 'pid' in qwargs:
        value = qwargs.pop('pid')
        pid.set(user, org, value)
    registry.signal('user_create', user=user, **qwargs)
    registry.signal('user_approval', user=user, send_invitation=send_invitation, raw_password=raw_password)

@transaction.atomic
def delete(**kwargs):
    user = get(**kwargs)
    if user == None:
        raise Exception('unknown user')
    registry.signal('user_delete', user=user)
    user.delete()

def delete_all(**kwargs):
    users = all(**kwargs)
    for user in users:
        user.delete()

def on_organization_deletion(**kwargs):
    org = kwargs['organization']
    delete_all(username__endswith='@%s' % org.suffix)

def send_approve_email(**kwargs):
    user = kwargs['user']
    send_invitation = False
    if 'send_invitation' in kwargs:
        send_invitation = kwargs['send_invitation']
    if not send_invitation:
        return
    raw_password = 'la que has indicat al registre'
    if 'raw_password' in kwargs:
        raw_password = kwargs['raw_password']
    org = organization.get_by_username(user.username)
    msg = u"""Com a membre de %s pots participar en el seu sistema de votació electrònica.

Entra a https://%s/identity/login/ i empra les següents credencials per a identificar-te:

  - Usuari: %s
  - Contrasenya: %s

Et recomanem canviar la contrasenya a 'Canviar contrasenya'.

Gràcies per fer-nos confiança,
%s
"""
    send_mail(u'Alta en sistema de votació en línia de %s' % org.name, msg % (org.name, org.domain, user.username.split('@')[0], raw_password, org.name), org.contact, [ user.email ], fail_silently=False)
