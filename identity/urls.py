from django.conf.urls import include, patterns, url

urlpatterns = patterns('',
    (r'^', include('identity.registration.backend.urls')),
)
