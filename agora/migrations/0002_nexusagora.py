# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('identity', '0003_auto_20150301_1208'),
        ('agora', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NexusAgora',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('agora', models.CharField(max_length=70)),
                ('link', models.ForeignKey(to='agora.AVLink')),
                ('nexus', models.ForeignKey(to='identity.Nexus')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
