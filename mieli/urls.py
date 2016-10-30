from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.views import static
from mieli.views import dashboard, featured, vote
from django.contrib.flatpages import views

urlpatterns = [
    url(r'^identity/', include('identity.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
    url(r'^dashboard/$', dashboard, name='dashboard'),
    url(r'^vote/(?P<path>[a-z0-9_-]+)$', vote, name='vote'),
    url(r'featured', featured, name='featured'),
    url(r'^(?P<url>.*)$', views.flatpage),
]
