# coding=utf-8
from django.contrib import admin

from .models import Stanowisko, Branza, Tags, PlJob, EngJob


class StanowiskoAdmin(admin.ModelAdmin):
    list_display = ('pl_job', 'eng_job', 'branza')

    list_filter = ('tags', 'branza')

    # raw_id_fields = ('pol_stanowisko','eng_stanowisko', 'branza',)
    # filter_horizontal = ('tags',)


admin.site.register(PlJob)
admin.site.register(EngJob)
admin.site.register(Branza)
admin.site.register(Tags)
admin.site.register(Stanowisko, StanowiskoAdmin )