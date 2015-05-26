from django.core.urlresolvers import reverse
from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from fora.mixins import LoginRequiredMixin
from threads.models import Thread


class ThreadMixin(object):

    def get_object(self):
        slug = self.kwargs.get('slug')
        try:
            return Thread.objects.get(slug=slug)
        except Thread.DoesNotExist:
            raise Http404('No Thread matches the given query.')


class NewThreadView(LoginRequiredMixin, CreateView):
    context_object_name = 'thread'
    model = Thread
    fields = ['subject', 'forum']

    def form_valid(self, form):
        f = form.save(commit=False)
        f.author = self.request.user
        f.save()
        return super(NewThreadView, self).form_valid(form)

    def get_success_url(self):
        return reverse('threads:show', kwargs={'slug': self.object.slug})


class ShowThreadView(ThreadMixin, DetailView):
    model = Thread
    context_object_name = 'thread'
