from django.conf.urls import url
from forums.views import NewForumView, ForumIndexView


urlpatterns = [
    url(r'^$', ForumIndexView.as_view(), name='index'),
    url(r'^new/$', NewForumView.as_view(), name='new'),
]
