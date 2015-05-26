from django.contrib.auth import (
    get_user_model, login as auth_login, logout as auth_logout
)
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormView
from django.views.generic import RedirectView
from users.forms import UserRegisterForm


class UserProfileView(DetailView):
    model = get_user_model()
    context_object_name = 'user'

    def get_object(self):
        return get_object_or_404(
            get_user_model(), username=self.kwargs.get('username'))


class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/user_register.html'

    def get_success_url(self):
        return reverse('users:profile', kwargs={
            'username': self.object.username})


class UserLoginView(FormView):
    template_name = 'users/user_login.html'
    form_class = AuthenticationForm

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        return super(UserLoginView, self).form_valid(form)

    def get_success_url(self):
        return reverse('forums:index')


class UserLogoutView(RedirectView):

    def get_redirect_url(self):
        return reverse('users:login')

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(UserLogoutView, self).get(request, *args, **kwargs)
