from django.conf.urls import url
from threads.views import NewThreadView, ShowThreadView


urlpatterns = [
    url(
        r'^new/$',
        NewThreadView.as_view(),
        name='new'
    ),
    url(
        r'^(?P<slug>[\w-]+)/$',
        ShowThreadView.as_view(),
        name='show'
    ),
]
