# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0009_auto_20150323_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='order',
            field=models.CharField(default=b'random', max_length=30),
            preserve_default=True,
        ),
    ]
