# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin1Codes',
            fields=[
                ('code', models.CharField(max_length=11, blank=True)),
                ('countrycode', models.CharField(max_length=2, blank=True)),
                ('admin1_code', models.CharField(max_length=10, blank=True)),
                ('name', models.CharField(max_length=200, blank=True)),
                ('alt_name_english', models.CharField(max_length=200, blank=True)),
                ('geonameid', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'admin1codes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Admin2Codes',
            fields=[
                ('code', models.CharField(max_length=50, blank=True)),
                ('countrycode', models.CharField(max_length=2, blank=True)),
                ('admin1_code', models.CharField(max_length=23, blank=True)),
                ('name', models.CharField(max_length=200, blank=True)),
                ('alt_name_english', models.CharField(max_length=200, blank=True)),
                ('geonameid', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'admin2codes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Alternatename',
            fields=[
                ('alternatenameid', models.IntegerField(serialize=False, primary_key=True)),
                ('geonameid', models.IntegerField(null=True, blank=True)),
                ('isolanguage', models.CharField(max_length=7, blank=True)),
                ('alternatename', models.CharField(max_length=200, blank=True)),
                ('ispreferredname', models.NullBooleanField()),
                ('isshortname', models.NullBooleanField()),
                ('iscolloquial', models.NullBooleanField()),
                ('ishistoric', models.NullBooleanField()),
            ],
            options={
                'db_table': 'alternatename',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Countryinfo',
            fields=[
                ('iso_alpha2', models.CharField(max_length=2, serialize=False, primary_key=True)),
                ('iso_alpha3', models.CharField(max_length=3, blank=True)),
                ('iso_numeric', models.IntegerField(null=True, blank=True)),
                ('fips_code', models.CharField(max_length=3, blank=True)),
                ('name', models.CharField(max_length=200, blank=True)),
                ('capital', models.CharField(max_length=200, blank=True)),
                ('areainsqkm', models.FloatField(null=True, blank=True)),
                ('population', models.IntegerField(null=True, blank=True)),
                ('continent', models.CharField(max_length=2, blank=True)),
                ('tld', models.CharField(max_length=10, blank=True)),
                ('currencycode', models.CharField(max_length=3, blank=True)),
                ('currencyname', models.CharField(max_length=20, blank=True)),
                ('phone', models.CharField(max_length=20, blank=True)),
                ('postalcode', models.CharField(max_length=100, blank=True)),
                ('postalcoderegex', models.CharField(max_length=200, blank=True)),
                ('languages', models.CharField(max_length=200, blank=True)),
                ('geonameid', models.IntegerField(null=True, blank=True)),
                ('neighbors', models.CharField(max_length=50, blank=True)),
                ('equivfipscode', models.CharField(max_length=3, blank=True)),
            ],
            options={
                'db_table': 'countryinfo',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Featurecodes',
            fields=[
                ('code', models.CharField(max_length=1, blank=True)),
                ('class_field', models.CharField(max_length=10, db_column=b'class', blank=True)),
                ('fcode', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('label', models.CharField(max_length=100, blank=True)),
                ('description', models.CharField(max_length=1000, blank=True)),
            ],
            options={
                'db_table': 'featurecodes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Geoname',
            fields=[
                ('geonameid', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200, blank=True)),
                ('asciiname', models.CharField(max_length=200, blank=True)),
                ('alternatenames', models.CharField(max_length=8000, blank=True)),
                ('latitude', models.FloatField(null=True, blank=True)),
                ('longitude', models.FloatField(null=True, blank=True)),
                ('fclass', models.CharField(max_length=1, blank=True)),
                ('fcode', models.CharField(max_length=10, blank=True)),
                ('country', models.CharField(max_length=2, blank=True)),
                ('cc2', models.CharField(max_length=60, blank=True)),
                ('admin1', models.CharField(max_length=20, blank=True)),
                ('admin2', models.CharField(max_length=80, blank=True)),
                ('admin3', models.CharField(max_length=20, blank=True)),
                ('admin4', models.CharField(max_length=20, blank=True)),
                ('population', models.BigIntegerField(null=True, blank=True)),
                ('elevation', models.IntegerField(null=True, blank=True)),
                ('gtopo30', models.IntegerField(null=True, blank=True)),
                ('timezone', models.CharField(max_length=40, blank=True)),
                ('moddate', models.DateField(null=True, blank=True)),
            ],
            options={
                'db_table': 'geoname',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Languagecodes',
            fields=[
                ('iso_639_3', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('iso_639_2', models.CharField(max_length=10, blank=True)),
                ('iso_639_1', models.CharField(max_length=2, blank=True)),
                ('name', models.CharField(max_length=1000, blank=True)),
            ],
            options={
                'db_table': 'languagecodes',
            },
            bases=(models.Model,),
        ),
    ]
