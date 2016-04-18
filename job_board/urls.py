from django.conf.urls import include, url
from . import views
from .feeds import LatestJobs

urlpatterns = [
    url(r'^$', views.job_list, name='index'),
    url(r'^vagas/rss/$', LatestJobs(), name='rss_feed'),
    url(r'^vagas/(?P<category>[a-zA-Z0-9_.-]+)/$', views.filter_by_category, name="filter_category"),
    url(r'^vagas/adicionar-vaga/$', views.job_create, name='job_create'),
    url(r'^vagas/(?P<slug>[\w-]+)$', views.job_detail, name='job_detail'),
]