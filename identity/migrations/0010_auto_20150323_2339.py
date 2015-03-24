# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('identity', '0009_organization_web'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='email_host_user',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
    ]
