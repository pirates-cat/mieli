from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django_tables2 import RequestConfig
from identity.tables import UserTable
from django.shortcuts import render
### TODO It shouldn't be here
from agora.api import agora_, user as agora_user
from mieli.api import user

def home(request):
    return render(request, 'mieli/index.html')

@user_passes_test(lambda u:u.is_staff, login_url='auth_login')
def dashboard(request):
    users = user.from_organization(request.organization, is_active=True, nexus=None)
    users_table = UserTable(users)
    RequestConfig(request).configure(users_table)
    return render(request, 'mieli/dashboard.html', {
        'users': users_table,
    })

@login_required(login_url='auth_login')
def vote(request, path):
    nexus = request.organization.main_nexus
    n_agora = agora_.get_by_nexus(nexus)
    n_agora.link.head('%s' % path) ## TODO <<<
    r = agora_user.login(n_agora.link, agora_user.get_agora_username(request.user))
    if 'errors' in r:
        return render(request, 'mieli/unauthorized_voter.html')
    print(r)
    return render(request, 'mieli/index.html')
