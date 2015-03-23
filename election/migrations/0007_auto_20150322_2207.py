# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0006_auto_20150322_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='description',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
