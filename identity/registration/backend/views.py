from registration.backends.default.views import ActivationView as BaseActivationView
from registration.backends.default.views import RegistrationView as BaseRegistrationView
from identity.registration.backend.forms import RegistrationForm
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from crispy_forms_foundation.layout import Submit
from django.core.urlresolvers import reverse
from crispy_forms.helper import FormHelper
from django.shortcuts import redirect
from django.db import transaction
from django.conf import settings
from identity.models import PID
from mieli.api import user
from mieli import registry

class RegistrationView(BaseRegistrationView):
    form_class = RegistrationForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect(reverse('auth_login'))
        return super(RegistrationView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect(reverse('auth_login'))
        return super(RegistrationView, self).post(request, *args, **kwargs)

    def handle_pid(self, user, organization, **pid_data):
        return PID.objects.create(user=user, organization=organization, **pid_data)

    def registration_allowed(self, request):
        return request.organization.registration_open

    @transaction.atomic
    def register(self, request, **cleaned_data):
        # TODO extract to hook
        pid_data = {}
        if request.organization.uid_field == 'pid':
            pid_data['value'] = cleaned_data.pop('pid_number')
            pid_data['document'] = cleaned_data.pop('pid_upload')
        new_user = super(RegistrationView, self).register(request, **cleaned_data)
        new_user.first_name = cleaned_data['first_name']
        new_user.last_name = cleaned_data['last_name']
        new_user.save()
        registry.signal('user_create', user=new_user)
        if len(pid_data) > 0:
            self.handle_pid(new_user, request.organization, **pid_data)
        return new_user

    def get_form(self, request, *args, **kwargs):
        form_class = self.get_form_class(request)
        form = super(RegistrationView, self).get_form(form_class)
        form.helper = FormHelper()
        form.helper.form_id = 'registration'
        form.helper.form_method = 'post'
        form.helper.form_action = 'registration_register'
        form.helper.add_input(Submit('submit', 'Submit'))
        return form

class ActivationView(BaseActivationView):
    pass

class ApproveView(TemplateView):
    http_method_names = ['get']
    template_name = 'registration/approve_complete.html'

    @method_decorator(user_passes_test(lambda u:u.is_staff, login_url='auth_login'))
    def dispatch(self, *args, **kwargs):
        return super(ApproveView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.approve(request, *args, **kwargs)
        return redirect('dashboard')

    def approve(self, request, user_pk):
        registry.signal('user_approval', user=user.get(pk=user_pk))
