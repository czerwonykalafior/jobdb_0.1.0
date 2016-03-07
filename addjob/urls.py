from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from .lookups_autocomplete import PlJobAutocomplete, EngJobAutocomplete, BranzaAutocomplete, TagsAutocomplete

urlpatterns = [

    url(r'^lista-zawodow/', views.job_list, name='job_list'),
    url(r'^dodaj-zawod/', views.add_job_form, name='add_job_form'),
    url(r'^lista-branz/', views.branze_list, name='branze_list'),
    url(r'^praca-w-branzy/(?P<branza_slug>[\w\-]+)/$', views.jobs_in_branza, name='job_in_branza'),
    url(r'^job-details/(?P<job_slug>[\w\-]+)/$', views.job_details, name='job_details'),

]

# autocomplete urls
urlpatterns += [

    url('pljob-autocomplete/$', PlJobAutocomplete.as_view(), name='pl_job-autocomplete', ),
    url('engjob-autocomplete/$', EngJobAutocomplete.as_view(), name='eng_job-autocomplete', ),
    url('branza-autocomplete/$', BranzaAutocomplete.as_view(), name='branza-autocomplete', ),
    url('tags-autocomplete/$', TagsAutocomplete.as_view(), name='tags-autocomplete', ),

]

# api

urlpatterns += [
    url(r'^b/$', views.BranzaList.as_view()),
    url(r'^b/$', views.BranzaList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
