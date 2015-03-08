# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agora', '0002_nexusagora'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nexusagora',
            name='link',
        ),
    ]
