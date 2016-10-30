# -*- coding: utf-8 -*-
from mieli.cli import MieliCommand
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from mieli.api import organization
from identity.api import pid
import codecs
import sys

UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)

class Command(MieliCommand):
    def invoke(self, *args, **options):
        with open('/home/agora/ac_voters.txt', 'r') as f:
            org = None
            voters = []
            for voter in f.readlines():
                voter = voter.strip()
                if org == None:
                    org = organization.get_by_username(voter)
                user = User.objects.get(username=voter)
                voters.append(user)
            for user in sorted(voters, key=lambda x: x.last_name):
                print(pid.get_by_user(org, user).value)
