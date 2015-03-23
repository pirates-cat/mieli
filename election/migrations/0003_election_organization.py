# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('identity', '0009_organization_web'),
        ('election', '0002_option_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='election',
            name='organization',
            field=models.ForeignKey(default=1, to='identity.Organization'),
            preserve_default=False,
        ),
    ]
