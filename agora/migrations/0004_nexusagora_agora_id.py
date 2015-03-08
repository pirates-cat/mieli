# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agora', '0003_remove_nexusagora_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='nexusagora',
            name='agora_id',
            field=models.IntegerField(default=7),
            preserve_default=False,
        ),
    ]
