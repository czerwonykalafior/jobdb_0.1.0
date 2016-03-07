from dal import autocomplete

from .models import Tags, Branza, PlJob, EngJob


class PlJobAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated():
        #     return Branza.objects.none()

        qs = PlJob.objects.all().order_by('name')

        if self.q:
            qs = qs.filter(name__contains=self.q)

        return qs


class EngJobAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated():
        #     return Branza.objects.none()

        qs = EngJob.objects.all().order_by('name')

        if self.q:
            qs = qs.filter(name__contains=self.q)

        return qs


class BranzaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated():
        #     return Branza.objects.none()

        qs = Branza.objects.all().order_by('name')

        if self.q:
            qs = qs.filter(name__contains=self.q)

        return qs


class TagsAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated():
        #     return Branza.objects.none()

        qs = Tags.objects.all().order_by('name')

        if self.q:
            qs = qs.filter(name__contains=self.q)

        return qs
