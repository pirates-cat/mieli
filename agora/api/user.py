from mieli.api import organization
from django.db import transaction
from django.conf import settings
from agora.api import link

@transaction.atomic
def create(user, **kwargs):
    org = organization.get_by_username(user.username)
    if org == None:
        raise Exception("unknown organization for user '%s'" % user.username)
    lnk = link.get(organization=org, user='agora')
    if lnk == None:
        raise Exception("no Agora Voting's admin link for organization '%s'" % org.domain)
    kwargs = {}
    kwargs['username'] = get_agora_username(user)
    kwargs['password1'] = kwargs['password2'] = settings.AGORA_DEFAULT_KEY
    kwargs['email'] = user.email
    kwargs['first_name'] = 'Mieli user'
    r = lnk.post('user/register', **kwargs)
    if 'errors' in r:
        raise Exception(r['errors'])
    login_kwargs = {}
    login_kwargs['identification'] = kwargs['username']
    login_kwargs['password'] = kwargs['password2']
    login_ = login(lnk, **login_kwargs)
    link_kwargs = {}
    link_kwargs['user'] = kwargs['username']
    link_kwargs['token'] = login_['apikey']
    link.create(org.domain, **link_kwargs)

def login(lnk, identification, password=settings.AGORA_DEFAULT_KEY):
    return lnk.post('user/login', identification=identification, password=password, __session=True)

@transaction.atomic
def delete(user, **kwargs):
    org = organization.get_by_username(user.username)
    if org == None:
        raise Exception("unknown organization for user '%s'" % user.username)
    link_kwargs = {}
    link_kwargs['user'] = get_agora_username(user)
    link.delete(org.domain, **link_kwargs)

def get_agora_username(user):
    return user.username.replace('@', '_at_')
