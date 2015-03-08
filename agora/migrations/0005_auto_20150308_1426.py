# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('identity', '0003_auto_20150301_1208'),
        ('agora', '0004_nexusagora_agora_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizationAgora',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField()),
                ('organization', models.ForeignKey(to='identity.Organization')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='avlink',
            name='organization',
        ),
        migrations.RemoveField(
            model_name='avlink',
            name='url',
        ),
        migrations.AddField(
            model_name='avlink',
            name='agora',
            field=models.ForeignKey(default=1, to='agora.OrganizationAgora'),
            preserve_default=False,
        ),
    ]
