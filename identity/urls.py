from django.conf.urls import include, url

urlpatterns = [
    url(r'^', include('identity.registration.backend.urls')),
]
