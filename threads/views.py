from django.core.urlresolvers import reverse
from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from threads.models import Thread


class ThreadMixin(object):

    def get_object(self):
        slug = self.kwargs.get('slug')
        try:
            return Thread.objects.get(slug=slug)
        except Thread.DoesNotExist:
            raise Http404('No Thread matches the given query.')


class NewThreadView(CreateView):
    model = Thread
    fields = ['subject', 'forum']

    def get_success_url(self):
        return reverse('threads:show', kwargs={'slug': self.object.slug})


class ShowThreadView(ThreadMixin, DetailView):
    model = Thread
