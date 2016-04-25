#!-*- coding: utf8 -*-

from django.db import models
from django.db.models.signals import pre_save, post_save

from django.utils.text import slugify

from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.core.urlresolvers import reverse

from django.template.loader import render_to_string

SALARY_RANGES = (
    ('n', 'A combinar'),
    ('j', 'Até R$ 2.500'),
    ('f', 'R$ 2.501 a R$ 3.500'),
    ('s', 'R$ 3.501 a R$ 6.000'),
    ('p', 'Acima de R$ 6.000'),
)

class Job(models.Model):
    published = models.BooleanField(default=False)
    title = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    url = models.URLField(blank=True)
    site = models.URLField(blank=True)
    email = models.EmailField()
    category = models.ForeignKey('Category')
    job_type = models.ForeignKey('JobType')
    salary = models.DecimalField(blank=True, default=0, max_digits=19, decimal_places=10)
    salary_range = models.CharField(blank=True, max_length=1, choices=SALARY_RANGES)
    description = models.TextField()
    about = models.TextField()
    skills = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title.encode('utf8')

    class Meta:
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return reverse("job_detail", kwargs={"slug": self.slug})


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title.encode('utf8')

    class Meta:
        verbose_name_plural = "categories"


class JobType(models.Model):
    name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name.encode('utf8')

# FUNCTIONS
def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Job.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = '%s-%s' %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def get_category_list():
    categories = Category.objects.filter().order_by('title')
    return categories

def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

def send_admin_notifications(sender, instance, created, **kwargs):
    if created:
        html_template = 'emails/notification.html'
        text_template = 'emails/notification.txt'

        subject, from_email, to = 'Alerta de nova mensagem.', 'contato@vagastirecife.com.br', 'csantos.machado@gmail.com'
        
        context = {
            'title': instance.title, 
            'timestamp': instance.timestamp
        }

        html_content = render_to_string(html_template, context)
        text_content = render_to_string(text_template, context)
        
        alert_mail = EmailMultiAlternatives(subject, text_content, from_email, [to])
        alert_mail.attach_alternative(html_content, 'text/html')
        alert_mail.send()
    else:
        pass

post_save.connect(send_admin_notifications, sender=Job)
pre_save.connect(pre_save_receiver, sender=Job)
pre_save.connect(pre_save_receiver, sender=Category)