# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('identity', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='domain',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='name',
        ),
        migrations.AddField(
            model_name='organization',
            name='site',
            field=models.ForeignKey(default=None, to='sites.Site'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organization',
            name='theme',
            field=models.CharField(default=1, max_length=32),
            preserve_default=False,
        ),
    ]
