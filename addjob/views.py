# coding=utf-8

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

import simplejson as json
from haystack.query import SearchQuerySet
from rest_framework import generics

from .serializers import BranzaSerializer
from .models import Stanowisko, Branza
from .forms import StanowiskoForm


def index(request):

    if request.method == 'POST':

        form = StanowiskoForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'addjob/thx.html')
        else:
            print form.errors
    else:
        form = StanowiskoForm()

    job_lst = Stanowisko.objects.all()
    job_number = job_lst.count()
    job_lst = job_lst.order_by('id').reverse()[:5]
    context_dict = {'form': form, 'jobs': job_lst, 'job_number': job_number}

    return render(request, 'addjob/base.html', context_dict)


def add_job_form(request):

    if request.method == 'POST':

        form = StanowiskoForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'addjob/thx.html')
        else:
            print form.errors
    else:
        form = StanowiskoForm()

    return render(request, 'addjob/form.html', {'form': form})


def branze_list(request):
    try:
        lst = Branza.objects.all().order_by('name')
    except Branza.DoesNotExist:
        lst = None

    return render(request, 'addjob/branze_list.html', {'list': lst})


def jobs_in_branza(request, branza_slug):
    # if request.method == 'GET':
    #     if 'id' in request.GET:
    #         id = request.GET['id']
    #         try:
    #             list = Stanowisko.objects.filter(branza = id)
    #         except ObjectDoesNotExist:
    #             print("Either the entry or blog doesn't exist.")
    branza = Branza.objects.get(slug=branza_slug)
    try:
        lst = Stanowisko.objects.filter(Q(branza=branza.id) | Q(sektor=branza.id))
    except Stanowisko.DoesNotExist:
        lst = None
    context_dict = {'branza': branza, 'list': lst}
    return render(request, 'addjob/jobs_in_branza.html', context_dict)


def job_list(request):
    try:
        lst = Stanowisko.objects.all().order_by('pl_job')
    except Stanowisko.DoesNotExist:
        lst = None
    return render(request, 'addjob/job_list.html', {'list': lst})


def job_details(request, job_slug):
    try:
        job = Stanowisko.objects.get(slug=job_slug)
    except Stanowisko.DoesNotExist:
        job = None
    #
    # if request.method == 'GET':
    #     if 'id' in request.GET:
    #         id = request.GET['id']
    #         try:
    #             job = Stanowisko.objects.get(id=id)
    #             print job
    #         except ObjectDoesNotExist:
    #             print id
    #             print ("Either the entry or job doesn't exist.")

    return render(request, 'addjob/job_details.html', {'job': job})


def autocomplete(request):
    sqs = SearchQuerySet().autocomplete(content_auto=request.GET.get('q', ''))[:5]
    suggestions = [result.title for result in sqs]
    # Make sure you return a JSON object, not a bare list.
    # Otherwise, you could be vulnerable to an XSS attack.
    the_data = json.dumps({
        'results': suggestions
    })
    return HttpResponse(the_data, content_type='application/json')

# class JSONResponse(HttpResponse):
#     """
#     An HttpResponse that renders its content into JSON.
#     """
#     def __init__(self, data, **kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse, self).__init__(content, **kwargs)

# TODO: Rest API
class BranzaList(generics.ListCreateAPIView):
    queryset = Branza.objects.all()
    serializer_class = BranzaSerializer


class BranzaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Branza.objects.all()
    serializer_class = BranzaSerializer
