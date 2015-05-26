from django.core.urlresolvers import reverse
from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from fora.mixins import LoginRequiredMixin
from forums.models import Forum


class ForumIndexView(ListView):
    context_object_name = 'forums'
    model = Forum


class NewForumView(LoginRequiredMixin, CreateView):
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


class UpdateForumView(LoginRequiredMixin, ForumMixin, UpdateView):
    context_object_name = 'forum'
    model = Forum
    fields = ['name', 'description']

    def get_success_url(self):
        return reverse('forums:index')


class ChangeForumVisibilityView(LoginRequiredMixin, UpdateView):
    context_object_name = 'forum'
    model = Forum
    fields = ['active']

    def get_success_url(self):
        return reverse('forums:index')


class ShowForumView(ForumMixin, DetailView):
    context_object_name = 'forum'
    model = Forum
