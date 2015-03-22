# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import identity.models


class Migration(migrations.Migration):

    dependencies = [
        ('identity', '0005_auto_20150315_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='alias',
            field=models.CharField(max_length=3, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pid',
            name='document',
            field=models.FileField(upload_to=identity.models.get_upload_path),
            preserve_default=True,
        ),
    ]
