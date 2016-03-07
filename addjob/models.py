# coding=utf-8
from __future__ import unicode_literals

from django.template.defaultfilters import slugify
from django.utils.encoding import smart_unicode
from django.db import models


class Branza(models.Model):
    name = models.CharField(max_length=100, help_text='Wybierz w jakiej branzy pracujesz.', unique=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Branza, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'branze'
        
    def __unicode__(self):
        return smart_unicode(self.name)


class Tags(models.Model):
    name = models.CharField(max_length=100, help_text='Z czym kojarzy Ci sie Twoja praca', unique=True)
    
    def __unicode__(self):
        return smart_unicode(self.name)


class PlJob(models.Model):
    name = models.CharField(verbose_name='Polska nazwa', max_length=100, help_text='Polska nazwa Twojego '
                                                                                   'stanowiska', unique=True)
    
    def __unicode__(self):
        return smart_unicode(self.name)


class EngJob(models.Model):
    name = models.CharField(verbose_name='Angielska nazwa', max_length=100, help_text='Polska nazwa Twojego stanowiska',
                            unique=True)
    
    def __unicode__(self):
        return smart_unicode(self.name)


class Stanowisko(models.Model):

    pl_job = models.ForeignKey(PlJob, verbose_name='Polska nazwa')
    eng_job = models.ForeignKey(EngJob, verbose_name='Angielska nazwa')
    branza = models.ForeignKey(Branza, related_name='branza_requests_created', )
    sektor = models.ForeignKey(Branza, related_name='sektors_requests_created', related_query_name='br')
    tags = models.ManyToManyField(Tags, related_name='tags_request_created')

    opis = models.TextField(verbose_name='opis stanowiska', max_length=1000, help_text='Na czym polega Twoja praca?')
    dzien = models.TextField(verbose_name='opis dnia', max_length=1000, help_text='Co robiles przez 8 godzin w pracy?')
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.id:
            string = " ".join([str(self.pl_job), str(self.eng_job)])
            self.slug = slugify(string)

        super(Stanowisko, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'stanowiska'
        
    def __unicode__(self):
        return smart_unicode(self.pl_job.name)
