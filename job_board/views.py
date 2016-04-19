#!-*- coding: utf8 -*-

from django.utils.six.moves.urllib.parse import quote_plus

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse

from .forms import CreateJobForm
from .models import Job, Category, get_category_list

def filter_by_category(request, category):
    categories = get_category_list()
    jobs = Job.objects.filter(category__slug__icontains=category)
    context = {
        'jobs': jobs,
        'categories': categories
    }
    return render(request, 'jobs/job_list.html', context)

def job_create(request):
    if request.method == 'POST':
        form = CreateJobForm(request.POST)
        if form.is_valid():
            job = form.save()
            messages.success(request, "Obrigado por anunciar sua vaga. Em breve ela estará disponível.")
            return redirect('index')
    else:
        form = CreateJobForm()
    return render(request, 'jobs/job_create.html', {'form': form})

def job_list(request):
    categories = Category.objects.all().order_by('title')
    jobs = Job.objects.filter(published=True)
    context = {
        'jobs': jobs,
        'categories': categories
    }
    return render(request, 'jobs/job_list.html', context)

def job_detail(request, slug):
    job = get_object_or_404(Job, slug=slug)
    if job.published:
        share_content = quote_plus("Achei esta #vaga de %s. Veja mais #vagas em www.vagastirecife.com.br" % (job.title))
        context = {
            'share_content': share_content,
            'job': job
        }
        return render(request, 'jobs/job_detail.html', context)
    else:
        messages.info(request, "Esta vaga ainda não está disponível. Tente novamente mais tarde.")
        return redirect('index')