from django.db import IntegrityError
from identity.models import PID
import re

def set(user, organization, value, document=None):
    if organization.uid_field != 'pid':   
        raise Exception("organization '%s' doesn't use personal identification as UID: current UID '%s'" % (organization.name, organization.uid_field))
    try:
        pid = get(organization, value)
        if pid.user != user:
            raise IntegrityError("PID is already associated to '%s'", user.username)
    except PID.DoesNotExist:
        if len(user.pid_set.all()) > 0:
            [pid.delete() for pid in user.pid_set.all()]
        pid = PID(user=user, organization=organization, value=value, document=document)
        pid.full_clean()
        pid.save()
    return pid

def get(organization, value=None):
    if organization.uid_field != 'pid':   
        raise Exception("organization '%s' doesn't use personal identification as UID: current UID '%s'" % (organization.name, organization.uid_field))
    value = re.sub('[^A-Z0-9]', '', value.upper())
    return PID.objects.get(organization=organization, value=value)
