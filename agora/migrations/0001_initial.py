# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('identity', '0003_auto_20150301_1208'),
    ]

    operations = [
        migrations.CreateModel(
            name='AVLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField()),
                ('user', models.CharField(max_length=32)),
                ('token', models.CharField(max_length=64)),
                ('organization', models.ForeignKey(to='identity.Organization')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
