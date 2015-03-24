from identity.models import Nexus
from django.db import models
from random import shuffle
import slugify
import time
import os

class Election(models.Model):
    title = models.CharField(max_length=140)
    nexus = models.ForeignKey(Nexus)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=140)

    @property
    def questions(self):
        return self.question_set.all()

    def __unicode__(self):
        return u'%s: %s' % (self.nexus, self.title)

def get_upload_path(instance, file_):
    file_name, file_ext = os.path.splitext(file_)
    return os.path.join('options', instance.question.election.nexus.organization.domain, time.strftime('%Y/%m/%d'), '%s%s' % (slugify.slugify(file_name), file_ext))

class Question(models.Model):
    election = models.ForeignKey(Election)
    description = models.TextField()
    # TODO add number (order)

    @property
    def options(self):
        ops = []
        for o in self.option_set.all():
            ops.append(o)
        shuffle(ops)
        return ops

    def __unicode__(self):
        return u'%s [%d]' % (self.election, self.pk)

class Option(models.Model):
    question = models.ForeignKey(Question)
    title = models.CharField(max_length=140)
    image = models.FileField(upload_to=get_upload_path, blank=True)
    document = models.FileField(upload_to=get_upload_path, blank=True)
    description = models.TextField(blank=True)
    web = models.URLField(blank=True)

    def __unicode__(self):
        return u'%s: %s' % (self.question, self.title)
