from django.db.models import Q
from geo.models import Admin1Codes, Admin2Codes, Geoname, Location

def load_administrative_divisions(country):
    return Admin1Codes.objects.filter(countrycode=country)

def load_administrative_2_divisions(country, admin1_code):
    return Admin2Codes.objects.filter(countrycode=country, admin1_code=admin1_code)

def load_places(country, admin1_code):
    return Geoname.objects.filter(country=country, admin1=admin1_code, fcode__startswith='PPL')

def find_by_name(name):
    result = Geoname.objects.filter(Q(name__iexact=name) | Q(asciiname__iexact=name), Q(fcode__startswith='PPL'))
    if len(result) == 0:
        result = Geoname.objects.filter(Q(name__iexact=name) | Q(asciiname__iexact=name), Q(fcode='ADM3'))
    return result

def find_by_user(user):
    return Location.objects.get(user=user)

def find(name, country):
    return find_by_name(name).filter(country=country)[:1]

def save(user, place, administrative_division_id=None):
    try:
        current = find_by_user(user)
        current.delete()
    except Location.DoesNotExist:
        pass
    admin1 = Admin1Codes.objects.get(countrycode=place.country, admin1_code=place.admin1)
    if administrative_division_id:
        admin2 = Admin2Codes.objects.get(geonameid=administrative_division_id)
    else:
        admin2 = Admin2Codes.objects.get(code="%s.%s.%s" % (place.country, place.admin1, place.admin2))
    location = Location(user=user, admin1=admin1, admin2=admin2, place=place)
    location.full_clean()
    location.save()
    return location
