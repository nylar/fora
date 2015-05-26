from django.contrib.auth import get_user_model
from django.test import TestCase
from forums.models import Forum
from posts.models import Post
from threads.models import Thread


class BaseTestCase(TestCase):

    _password = 'secret'

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='user', password=self._password)

    def tearDown(self):
        get_user_model().objects.all().delete()
        Post.objects.all()
        Thread.objects.all().delete()
        Forum.objects.all().delete()
        super(BaseTestCase, self).tearDown()

    def _add_session_to_request(self, request):
        from django.contrib.sessions.middleware import SessionMiddleware
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
