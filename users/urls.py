from django.conf.urls import url
from users.views import (
    UserProfileView, UserLoginView, UserLogoutView, UserRegisterView
)


urlpatterns = [
    url(
        r'^login/$',
        UserLoginView.as_view(),
        name='login'
    ),
    url(
        r'^logout/$',
        UserLogoutView.as_view(),
        name='logout'
    ),
    url(
        r'^register/$',
        UserRegisterView.as_view(),
        name='register'
    ),
    url(
        r'^(?P<username>[\w-]+)/$',
        UserProfileView.as_view(),
        name='profile'
    ),
]
