#!-*- coding: utf8 -*-

from django.contrib.sitemaps import Sitemap

from .models import Job

class JobSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Job.objects.filter(published=True)

    def lastmod(self, obj):
        return obj.timestamp