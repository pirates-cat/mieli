from django.core.mail.backends.smtp import EmailBackend as BaseEmailBackend
from django.conf import settings
from identity import helpers

class EmailBackend(BaseEmailBackend):
    def __init__(self, host=None, port=None, username=None, password=None,
                 use_tls=None, fail_silently=False, use_ssl=None, timeout=None,
                 ssl_keyfile=None, ssl_certfile=None,
                 **kwargs):
        kwargs['fail_silently'] = fail_silently
        organization_ = helpers.get_current_organization()
        kwargs['host'] = host or organization_.email_host
        kwargs['password'] = password or organization_.email_host_password
        kwargs['username'] = username or organization_.email_host_user
        kwargs['port'] = port or organization_.email_port
        kwargs['use_ssl'] = use_ssl or organization_.email_use_ssl
        kwargs['use_tls'] = use_tls or organization_.email_use_tls
        if ssl_keyfile or ssl_certfile:
            raise ValueError('SSL keyfile and certificate not supported.')
        settings.DEFAULT_FROM_EMAIL = organization_.contact
        super(EmailBackend, self).__init__(**kwargs)

    def _send(self, email_message):
        if email_message.from_email == 'webmaster@localhost':
            organization_ = helpers.get_current_organization()
            email_message.from_email = organization_.contact
        return super(EmailBackend, self)._send(email_message)
