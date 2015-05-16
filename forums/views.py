from django.core.urlresolvers import reverse
from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from forums.models import Forum


class ForumIndexView(ListView):
    model = Forum


class NewForumView(CreateView):
    model = Forum
    fields = ['name', 'description', 'active']

    def get_success_url(self):
        return reverse('forums:index')


class ForumMixin(object):

    def get_object(self):
        slug = self.kwargs.get('slug')
        try:
            return Forum.visible.get(slug=slug)
        except Forum.DoesNotExist:
            raise Http404('No Forum matches the given query.')


class UpdateForumView(ForumMixin, UpdateView):
    model = Forum
    fields = ['name', 'description']

    def get_success_url(self):
        return reverse('forums:index')


class ChangeForumVisibilityView(UpdateView):
    model = Forum
    fields = ['active']

    def get_success_url(self):
        return reverse('forums:index')


class ShowForumView(ForumMixin, DetailView):
    model = Forum
