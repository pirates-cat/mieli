from django.db import models
from django.contrib.auth.models import User

class Admin1Codes(models.Model):
    code = models.CharField(max_length=11, blank=True)
    countrycode = models.CharField(max_length=2, blank=True)
    admin1_code = models.CharField(max_length=10, blank=True)
    name = models.CharField(max_length=200, blank=True)
    alt_name_english = models.CharField(max_length=200, blank=True)
    geonameid = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'admin1codes'


class Admin2Codes(models.Model):
    code = models.CharField(max_length=50, blank=True)
    countrycode = models.CharField(max_length=2, blank=True)
    admin1_code = models.CharField(max_length=23, blank=True)
    name = models.CharField(max_length=200, blank=True)
    alt_name_english = models.CharField(max_length=200, blank=True)
    geonameid = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'admin2codes'

class Alternatename(models.Model):
    alternatenameid = models.IntegerField(primary_key=True)
    geonameid = models.IntegerField(blank=True, null=True)
    isolanguage = models.CharField(max_length=7, blank=True)
    alternatename = models.CharField(max_length=200, blank=True)
    ispreferredname = models.NullBooleanField()
    isshortname = models.NullBooleanField()
    iscolloquial = models.NullBooleanField()
    ishistoric = models.NullBooleanField()

    class Meta:
        db_table = 'alternatename'

class Countryinfo(models.Model):
    iso_alpha2 = models.CharField(primary_key=True, max_length=2)
    iso_alpha3 = models.CharField(max_length=3, blank=True)
    iso_numeric = models.IntegerField(blank=True, null=True)
    fips_code = models.CharField(max_length=3, blank=True)
    name = models.CharField(max_length=200, blank=True)
    capital = models.CharField(max_length=200, blank=True)
    areainsqkm = models.FloatField(blank=True, null=True)
    population = models.IntegerField(blank=True, null=True)
    continent = models.CharField(max_length=2, blank=True)
    tld = models.CharField(max_length=10, blank=True)
    currencycode = models.CharField(max_length=3, blank=True)
    currencyname = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    postalcode = models.CharField(max_length=100, blank=True)
    postalcoderegex = models.CharField(max_length=200, blank=True)
    languages = models.CharField(max_length=200, blank=True)
    geonameid = models.IntegerField(blank=True, null=True)
    neighbors = models.CharField(max_length=50, blank=True)
    equivfipscode = models.CharField(max_length=3, blank=True)

    class Meta:
        db_table = 'countryinfo'

class Featurecodes(models.Model):
    code = models.CharField(max_length=1, blank=True)
    class_field = models.CharField(db_column='class', max_length=10, blank=True)  # Field renamed because it was a Python reserved word.
    fcode = models.CharField(primary_key=True, max_length=10)
    label = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=1000, blank=True)

    class Meta:
        db_table = 'featurecodes'

class Geoname(models.Model):
    geonameid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, blank=True)
    asciiname = models.CharField(max_length=200, blank=True)
    alternatenames = models.CharField(max_length=8000, blank=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    fclass = models.CharField(max_length=1, blank=True)
    fcode = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=2, blank=True)
    cc2 = models.CharField(max_length=60, blank=True)
    admin1 = models.CharField(max_length=20, blank=True)
    admin2 = models.CharField(max_length=80, blank=True)
    admin3 = models.CharField(max_length=20, blank=True)
    admin4 = models.CharField(max_length=20, blank=True)
    population = models.BigIntegerField(blank=True, null=True)
    elevation = models.IntegerField(blank=True, null=True)
    gtopo30 = models.IntegerField(blank=True, null=True)
    timezone = models.CharField(max_length=40, blank=True)
    moddate = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'geoname'

class Languagecodes(models.Model):
    iso_639_3 = models.CharField(primary_key=True, max_length=10)
    iso_639_2 = models.CharField(max_length=10, blank=True)
    iso_639_1 = models.CharField(max_length=2, blank=True)
    name = models.CharField(max_length=1000, blank=True)

    class Meta:
        db_table = 'languagecodes'

class Location(models.Model):
    user = models.ForeignKey(User)
    admin1 = models.ForeignKey(Admin1Codes)
    admin2 = models.ForeignKey(Admin2Codes)
    place = models.ForeignKey(Geoname)

