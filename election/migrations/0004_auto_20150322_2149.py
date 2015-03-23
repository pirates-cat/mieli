# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('identity', '0009_organization_web'),
        ('election', '0003_election_organization'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='election',
            name='organization',
        ),
        migrations.AddField(
            model_name='election',
            name='nexus',
            field=models.ForeignKey(default=1, to='identity.Nexus'),
            preserve_default=False,
        ),
    ]
