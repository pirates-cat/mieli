from mieli.api import organization
from django.conf import settings
from agora.api import link

def create(user, **kwargs):
    org = organization.get_by_username(user.username)
    if org == None:
        raise Exception("unknown organization for user '%s'" % user.username)
    lnk = link.get(organization=org)
    if lnk == None:
        raise Exception("no Agora Voting link for organization '%s'" % org.domain)
    kwargs = {}
    kwargs['username'] = user.username.replace('@', '_at_')
    kwargs['password1'] = kwargs['password2'] = settings.AGORA_DEFAULT_KEY
    kwargs['email'] = user.email
    kwargs['first_name'] = 'Mieli user'
    lnk.post('user/register', **kwargs)
