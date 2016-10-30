"""
THIS IS AN AUTO-GENERATED FILE. CHANGES YOU MAKE HERE WILL BE OVERWRITTEN
IF YOU WANT TO INTRODUCE MODIFICATIONS EDIT THE settings.py.j2 FILE
LOCATED IN THE deploy/roles/application/templates/django DIRECTORY.
"""
import os
from datetime import timedelta

# The base dir is the parent of the directory. If we were to change the inner
# dirname to abspath we would have to append "..".
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = "canihazchangeplz?"

DEBUG = True
TEMPLATE_DEBUG = True

# django will recursively search in directories for other template folders
TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'),)

ALLOWED_HOSTS = []
ROOT_URLCONF = 'mieli.urls'

from django_mu.models import SiteID
SITE_ID = SiteID()

WSGI_APPLICATION = 'mieli.wsgi.application'

# Installed apps
DEFAULT_APPS = (
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
)

FIRST_PARTY_APPS = (
    'mieli',
    'identity',
    'agora',
    'election',
    'geo',
)

THIRD_PARTY_APPS = (
    'gunicorn',
    'registration',
    'crispy_forms',
    'crispy_forms_foundation',
    'django_tables2',
    'django.contrib.flatpages',
)

INSTALLED_APPS = DEFAULT_APPS + FIRST_PARTY_APPS + THIRD_PARTY_APPS


# Middleware classes
MIDDLEWARE_CLASSES = (
    'django_mu.middleware.MultiSiteMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'mieli.middleware.MieliMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
)


#Template context processors
DEFAULT_TEMPLATE_CONTEXT_PROCESSORS = (
    "django.template.context_processors.debug",
    "django.template.context_processors.request",
    "django.contrib.auth.context_processors.auth",
    "django.contrib.messages.context_processors.messages",
)

CUSTOM_TEMPLATE_CONTEXT_PROCESSORS = ()

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_TEMPLATE_CONTEXT_PROCESSORS + CUSTOM_TEMPLATE_CONTEXT_PROCESSORS

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': TEMPLATE_CONTEXT_PROCESSORS,
        },
    },
]


# Email backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Static file configuration
# It must be an external path.
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATIC_URL = '/static/'


# Media files configuration
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# Add a random suffix '-suffix' to avoid leaks
MEDIA_URL = '/media/'


# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mieli',
        'USER': 'mieli',
        'PASSWORD': 'mieli',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

#  Optimizes read heavy PG workload, install only if PG
if 'postgresql_psycopg2' == 'postgresql_psycopg2':
    DATABASES['default']['OPTIONS'] = {'autocommit': True}

# Password storage
# https://docs.djangoproject.com/es/1.10/topics/auth/passwords/#auth-password-storage

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'mieli.hashers.LDAPSHA1PasswordHasher',
    'django.contrib.auth.hashers.UnsaltedSHA1PasswordHasher',
    'django.contrib.auth.hashers.UnsaltedMD5PasswordHasher'
]

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.'
        'UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': [],
        }
    },
    'loggers': {
        'django': {
            'handlers': ['null'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}


# Django-Registration
ACCOUNT_ACTIVATION_DAYS = 7
LOGIN_REDIRECT_URL = '/'


# Crispy Forms
CRISPY_TEMPLATE_PACK = 'foundation-5'


# Mieli
MAIN_NEXUS = 'Main'
AGORA_ADMIN_USER = 'agora'
AGORA_DEFAULT_KEY = 'canihazchangeplz?'
AGORA_BACKEND_COOKIE = 'agora_backend'

try:
    from mieli.custom_settings import *
except ImportError:
    pass
