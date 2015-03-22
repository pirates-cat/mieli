# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.sites.models


class Migration(migrations.Migration):

    dependencies = [
        ('identity', '0007_organization_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='email_host',
            field=models.CharField(blank=True, max_length=100, validators=[django.contrib.sites.models._simple_domain_name_validator]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='organization',
            name='email_host_password',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='organization',
            name='email_host_user',
            field=models.CharField(max_length=30, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='organization',
            name='email_port',
            field=models.IntegerField(default=587),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='organization',
            name='email_use_ssl',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='organization',
            name='email_use_tls',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
