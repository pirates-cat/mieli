from django.contrib import admin
from election.models import *

admin.site.register(Election)
admin.site.register(Question)
admin.site.register(Option)
