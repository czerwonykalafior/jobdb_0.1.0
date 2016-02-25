import datetime
from haystack import indexes
from .models import Stanowisko


class StanowiskoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    pl_job = indexes.CharField(model_attr='pl_job')
    eng_job = indexes.CharField(model_attr='eng_job')
    branza  = indexes.CharField(model_attr='branza')
    sektor = indexes.CharField(model_attr='sektor')
    # opis = indexes.CharField(model_attr='opis')
    dzien = indexes.CharField(model_attr='dzien')
    # tags = indexes.CharField(model_attr='tags')
    content_auto = indexes.EdgeNgramField(model_attr='opis')

    def get_model(self):
        return Stanowisko

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""

        return self.get_model().objects.all()

