# coding=utf-8
from dal import autocomplete
from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Stanowisko, Tags, PlJob, EngJob

# TODO: Zmienic pojawianie sie 'Create" przy dodawaniu nowego wpisu
# TODO: Jesli wpis istnieje w bazie nie powinno sie pojawiac 'Create'
# TODO: Opisy formularza w polu wpisywania


class StanowiskoForm(ModelForm):


    class Meta:
        model = Stanowisko
        fields = ('pl_job', 'eng_job', 'branza', 'sektor', 'tags', 'opis', 'dzien')
        widgets = {
            'pl_job': autocomplete.ModelSelect2(url='pl_job-autocomplete'),
            'eng_job': autocomplete.ModelSelect2(url='eng_job-autocomplete'),
            'branza': autocomplete.ModelSelect2(url='branza-autocomplete'),
            'sektor': autocomplete.ModelSelect2(url='branza-autocomplete'),
            'tags': autocomplete.ModelSelect2Multiple(url='tags-autocomplete'),
            'opis': forms.Textarea(attrs={'cols': 40, 'rows': 11}),
            'dzien': forms.Textarea(attrs={'cols': 40, 'rows': 11}),
        }

        labels = {
            'branza': "Z jakiej branży jest to stanowisko",
            'sektor': "W jakim sektorze pracujesz jako ... ",
            'opis': "Opisz swoje stanowisko",
            'dzien': "Opisz jeden dzień z pracy"
        }
