from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseServerError
from agora.api import agora_, user as agora_user # TODO <- this shouldn't be here
from django_tables2 import RequestConfig
from identity.tables import UserTable
from django.shortcuts import render, redirect
from django.conf import settings
from mieli.api import user
import cookies

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
    booth = '%s/%s/election/%s/vote' % (settings.AGORA_ADMIN_USER, n_agora.agora, path)
    try:
        n_agora.link.head(booth)
    except:
        raise Http404('Vote does not exist.')
    r = agora_user.login(n_agora.link, agora_user.get_agora_username(request.user))
    if 'errors' in r:
        return render(request, 'mieli/unauthorized_voter.html')
    session = r['__session']
    if session == None:
        return HttpResponseServerError('Error while logging in you in the backend.')
    c = cookies.Cookies()
    c.parse_response(session)
    if not settings.AGORA_BACKEND_COOKIE in c:
        return HttpResponseServerError('Unexpected behavoir in backend.')
    try:
        abc = c[settings.AGORA_BACKEND_COOKIE]
    except KeyError:
        return HttpResponseServerError('Unexpected error getting backend cookie.')
    response = redirect('%s/%s' % (n_agora.link.url, booth))
    response.set_cookie(settings.AGORA_BACKEND_COOKIE, value=abc.value, max_age=abc.max_age, expires=abc.expires, path=abc.path, domain=request.site.domain, secure=abc.secure, httponly=abc.httponly)
    return response
