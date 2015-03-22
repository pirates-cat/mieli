from registration.forms import RegistrationForm as BaseRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from crispy_forms_foundation.layout import Submit
from crispy_forms.helper import FormHelper
from identity import helpers
from mieli import registry

class RegistrationForm(BaseRegistrationForm):
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        registry.apply_filter('registration_form', form=self)

    def clean_username(self):
        self.cleaned_data['username'] = '%s@%s' % (self.cleaned_data['username'], helpers.get_current_organization().suffix)
        return super(RegistrationForm, self).clean_username()

    def clean(self):
        registry.signal('registration_clean', form=self)
        return super(RegistrationForm, self).clean()

class LoginForm(AuthenticationForm):
    helper = FormHelper()
    helper.form_id = 'login'
    helper.form_method = 'post'
    helper.form_action = 'auth_login'
    helper.add_input(Submit('submit', 'Submit'))

    def clean(self):
        self.cleaned_data['username'] = '%s@%s' % (self.cleaned_data['username'], helpers.get_current_organization().suffix)
        return super(LoginForm, self).clean()
