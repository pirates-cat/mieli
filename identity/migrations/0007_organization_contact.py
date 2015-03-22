# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('identity', '0006_auto_20150322_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='contact',
            field=models.EmailField(max_length=75, blank=True),
            preserve_default=True,
        ),
    ]
