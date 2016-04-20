#!-*- coding: utf8 -*-

from django.contrib import admin
from django.utils.text import slugify

from job_board.models import Job, Category, JobType


class JobAdmin(admin.ModelAdmin):
    ordering = ['-timestamp']
    readonly_fields=('slug',)

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('slug',)

admin.site.register(Job, JobAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(JobType)