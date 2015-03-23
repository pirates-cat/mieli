# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0004_auto_20150322_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='election',
            name='description',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
