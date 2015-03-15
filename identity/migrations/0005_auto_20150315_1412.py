# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('identity', '0004_pid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pid',
            old_name='image',
            new_name='document',
        ),
    ]
