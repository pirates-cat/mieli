# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('identity', '0008_auto_20150322_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='web',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
    ]
