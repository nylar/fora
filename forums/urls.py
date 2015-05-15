from django.conf.urls import url
from forums.views import (
    NewForumView, ForumIndexView, UpdateForumView, ChangeForumVisibilityView
)


urlpatterns = [
    url(
        r'^$',
        ForumIndexView.as_view(),
        name='index'
    ),
    url(
        r'^new/$',
        NewForumView.as_view(),
        name='new'
    ),
    url(
        r'^(?P<slug>[\w-]+)/update/$',
        UpdateForumView.as_view(),
        name='update'
    ),
    url(
        r'^(?P<slug>[\w-]+)/visibility/$',
        ChangeForumVisibilityView.as_view(),
        name='visibility'
    ),
]
