from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse

from .models import Job

class LatestJobs(Feed):
    title = 'Vagas TI Recife - Últimas vagas e oportunidades em TI no Recife'
    link = '/'
    # description = 'Veja as últimas vagas e oportunidades anunciadas para a área de TI em Recife/PE'
    # description_template = 'feeds/feed.html'

    def items(self):
        return Job.objects.all().order_by('-timestamp')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_link(self, item):
        return reverse('job_detail', args=[item.slug])