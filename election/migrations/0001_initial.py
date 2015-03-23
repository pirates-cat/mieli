# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import election.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Election',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=140)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=140)),
                ('image', models.FileField(upload_to=election.models.get_upload_path, blank=True)),
                ('document', models.FileField(upload_to=election.models.get_upload_path, blank=True)),
                ('description', models.TextField()),
                ('web', models.URLField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
