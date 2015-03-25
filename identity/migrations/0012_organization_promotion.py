# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('identity', '0011_auto_20150324_2329'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='promotion',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
