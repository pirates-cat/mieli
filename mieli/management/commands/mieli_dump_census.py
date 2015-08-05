# -*- coding: utf-8 -*-
from mieli.cli import MieliCommand
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
import codecs
import sys

UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)

class Command(MieliCommand):
    def invoke(self, *args, **options):
        with open('/home/agora/ac_voters.txt', 'r') as f:
            print("<html><head><title>Cens</title></head><body><ul>")
            voters = []
            for voter in f.readlines():
                voter = voter.strip()
                user = User.objects.get(username=voter)
                voters.append(user)
            for user in sorted(voters, key=lambda x: x.first_name):
                print("<li>%s %s (%s)</li>" % (user.first_name, user.last_name, user.email))
            print("</ul></body></html>")
