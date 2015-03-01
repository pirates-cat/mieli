# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('identity', '0002_auto_20150228_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='uid_field',
            field=models.CharField(default=b'email', max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organization',
            name='theme',
            field=models.CharField(default=b'default', max_length=32),
            preserve_default=True,
        ),
    ]
