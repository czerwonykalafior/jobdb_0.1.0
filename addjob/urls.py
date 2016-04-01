from django.conf.urls import url
from django.views import generic

from rest_framework.urlpatterns import format_suffix_patterns

from addjob.forms import StanowiskoForm
from addjob.models import PlJob, Tags
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

    url('pljob-autocomplete/$', PlJobAutocomplete.as_view(model=PlJob, create_field='name'), name='pl_job-autocomplete', ),
    url(r'^engjob-autocomplete/$', EngJobAutocomplete.as_view(create_field='name'), name='eng_job-autocomplete', ),
    url(r'^branza-autocomplete/$', BranzaAutocomplete.as_view(), name='branza-autocomplete', ),
    url(r'^tags-autocomplete/$', TagsAutocomplete.as_view(model=Tags, create_field='name'), name='tags-autocomplete', ),

]

# api

urlpatterns += [
    url(r'^b/$', views.BranzaList.as_view()),
    url(r'^b/$', views.BranzaList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
