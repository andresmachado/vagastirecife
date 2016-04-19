from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.core.urlresolvers import reverse


class Job(models.Model):
    published = models.BooleanField(default=False)
    title = models.CharField(max_length=140)
    company = models.CharField(max_length=140)
    url = models.URLField(blank=True)
    site = models.URLField(blank=True)
    email = models.EmailField()
    category = models.ForeignKey('Category')
    job_type = models.ForeignKey('JobType')
    salary = models.DecimalField(default=0, max_digits=19, decimal_places=2)
    description = models.TextField()
    about = models.TextField()
    skills = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return reverse("job_detail", kwargs={"slug": self.slug})


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "categories"


class JobType(models.Model):
    name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name

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


pre_save.connect(pre_save_receiver, sender=Job)
pre_save.connect(pre_save_receiver, sender=Category)