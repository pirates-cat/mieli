"""
THIS IS AN AUTO-GENERATED FILE. CHANGES YOU MAKE HERE WILL BE OVERWRITTEN
IF YOU WANT TO INTRIDUCE MODIFICATIONS EDIT THE settings_test.py.j2 FILE
LOCATED IN THE deploy/roles/application/templates/django DIRECTORY.
"""

import os
import logging

from mieli.settings import *

DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3'}
PASSWORD_HASHERS = (
    'django_plainpasswordhasher.PlainPasswordHasher',
)

DEFAULT_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
)

FIRST_PARTY_APPS = (
    'mieli',
)

THIRD_PARTY_APPS = (
)

INSTALLED_APPS = DEFAULT_APPS + FIRST_PARTY_APPS + THIRD_PARTY_APPS


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.common.CommonMiddleware',
)

DEBUG = True
TEMPLATE_DEBUG = True

logging.disable(logging.CRITICAL)

TEST_RUNNER = 'django_coverage.coverage_runner.CoverageRunner'

COVERAGE_MODULE_EXCLUDES = ['__init__',

                            'django',
                            'migrations',
                            'management',

                            'locale$',
                            'tests$',
                            'settings$',
                            'settings_test$',

                            'urls$',
                            'wsgi$']

COVERAGE_BADGE_TYPE = None
