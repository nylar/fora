from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView


class UserProfileView(DetailView):
    model = get_user_model()
    context_object_name = 'user'

    def get_object(self):
        return get_object_or_404(
            get_user_model(), username=self.kwargs.get('username'))
