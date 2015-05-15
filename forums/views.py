from django.core.urlresolvers import reverse
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


class UpdateForumView(UpdateView):
    model = Forum
    fields = ['name', 'description']

    def get_success_url(self):
        return reverse('forums:index')
