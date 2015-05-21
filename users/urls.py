from django.conf.urls import url
from users.views import UserProfileView, UserRegisterView


urlpatterns = [
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
