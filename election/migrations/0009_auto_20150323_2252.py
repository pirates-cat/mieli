# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0008_auto_20150322_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='election',
            name='slug',
            field=models.SlugField(max_length=140),
            preserve_default=True,
        ),
    ]
