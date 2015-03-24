# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import identity.models


class Migration(migrations.Migration):

    dependencies = [
        ('identity', '0010_auto_20150323_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='registration_open',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pid',
            name='document',
            field=models.FileField(upload_to=identity.models.get_upload_path, blank=True),
            preserve_default=True,
        ),
    ]
