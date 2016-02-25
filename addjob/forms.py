# coding=utf-8
from dal import autocomplete
from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from models import Stanowisko, Tags, PlJob, EngJob



class PlJobCreateField(autocomplete.CreateModelField):
    def create_value(self, value):
        try:
            t = PlJob.objects.create(name=value).pk
        except:
            raise ValidationError
        return t

class EngJobCreateField(autocomplete.CreateModelField):
    def create_value(self, value):
        return EngJob.objects.create(name=value).pk

class TagCreateMultipleField(autocomplete.CreateModelMultipleField):
    def create_value(self, value):
        return Tags.objects.create(name=value).pk


class StanowiskoForm(ModelForm):

    pl_job = PlJobCreateField(
            queryset = PlJob.objects.all(),
            required = True,  # leave out if your model field doesn't have blank=True
            widget = autocomplete.ModelSelect2(url='pl_job-autocomplete'),
            label = 'Polska nazwa Twojego stanowiska'

    )

    eng_job = EngJobCreateField(
            required = True,  # leave out if your model field doesn't have blank=True
            queryset = EngJob.objects.all(),
            widget = autocomplete.ModelSelect2(url='eng_job-autocomplete'),
            label = 'Angielska nazwa'
    )

    tags = TagCreateMultipleField(
            required = False,  # leave out if your model field doesn't have blank=True
            queryset = Tags.objects.all(),
            widget = autocomplete.ModelSelect2Multiple(url='tags-autocomplete'),
            label = 'Otaguj'
    )


    class Meta:
        model = Stanowisko
        fields = ('pl_job', 'eng_job', 'branza', 'sektor', 'tags', 'opis', 'dzien')
        widgets = {

            'branza': autocomplete.ModelSelect2(url='branza-autocomplete'),
            'sektor': autocomplete.ModelSelect2(url='branza-autocomplete'),
            'opis' : forms.Textarea(attrs={'cols': 48, 'rows': 11}),
            'dzien' : forms.Textarea(attrs={'cols': 48, 'rows': 11}),
        }
        labels = {
            'branza': ("Z jakiej branży jest to stanowisko"),
            'sektor': ("W jakim sektorze pracujesz jako ... "),
            'opis': ("Opisz swoje stanowisko"),
            'dzien': ("Opisz jeden dzień z pracy")
        }
