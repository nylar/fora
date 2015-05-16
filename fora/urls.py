from django.conf.urls import include, url


urlpatterns = [
    url(r'^forums/', include('forums.urls', namespace='forums')),
    url(r'^threads/', include('threads.urls', namespace='threads')),
]
