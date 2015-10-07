from django.views.generic import TemplateView, ListView, DetailView

import models


class IndexView(TemplateView):
    template_name = 'posting/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        try:
            latest = models.ComicStrip.objects.latest()
        except models.ComicStrip.DoesNotExist:
            latest = None

        context['latest'] = latest
        return context


class AboutView(TemplateView):
    template_name = 'posting/about.html'


class ComicStripListView(ListView):
    model = models.ComicStrip
    paginate_by = 5


class ComicStripDetailView(DetailView):
    model = models.ComicStrip
