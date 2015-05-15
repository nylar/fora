from django.conf.urls import url
from forums.views import NewForumView, ForumIndexView, UpdateForumView


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
]
