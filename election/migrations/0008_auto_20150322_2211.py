# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0007_auto_20150322_2207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='option',
            name='slug',
        ),
        migrations.AddField(
            model_name='election',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
