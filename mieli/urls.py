from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    url(r'^identity/', include('identity.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}, name='media'),
    url(r'^dashboard/$', 'mieli.views.dashboard', name='dashboard'),
    url(r'^vote/(?P<path>[a-z0-9]+)$', 'mieli.views.vote', name='vote'),
    url(r'^$', 'mieli.views.home', name='home'),
)
