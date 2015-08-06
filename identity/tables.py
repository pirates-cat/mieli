from mieli.helpers import get_current_organization
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from identity.models import PID
import django_tables2 as tables

class UserTable(tables.Table):
    pid = tables.Column(accessor='id', verbose_name='PID', empty_values=())
    auth = tables.Column(accessor='id', verbose_name='Authorize', empty_values=())
    organization = get_current_organization()

    def render_pid(self, value):
        try:
            pid = PID.objects.get(organization=self.organization, user__id=value)
            return mark_safe('<a target="_blank" href="%s">%s</a>' % (reverse('media', kwargs={'path': pid.document}), pid.value))
        except PID.DoesNotExist:
            return ''

    def render_auth(self, value):
        return mark_safe('<a href="%s">Autoritza</a>' % reverse('auth_approve', kwargs={'user_pk': value}))

    class Meta:
        model = User
        attrs = {"class": "paleblue"}
        fields = ('username', 'first_name', 'last_name', 'email', 'is_active', )
