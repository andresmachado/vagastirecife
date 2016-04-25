#!-*- coding: utf8 -*-

from django.contrib import admin
from django.utils.text import slugify

from job_board.models import Job, Category, JobType


def publish_jobs(modeladmin, request, queryset):
    queryset.update(published=True)
publish_jobs.short_description = 'Publicar vagas'


class JobAdmin(admin.ModelAdmin):
    ordering = ['-timestamp']
    readonly_fields=('slug',)
    list_display = ('title', 'published', 'timestamp')
    actions = [publish_jobs]

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('slug',)

admin.site.register(Job, JobAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(JobType)