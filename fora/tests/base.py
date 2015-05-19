from django.test import TestCase
from forums.models import Forum
from posts.models import Post
from threads.models import Thread


class BaseTestCase(TestCase):

    def tearDown(self):
        Post.objects.all()
        Thread.objects.all().delete()
        Forum.objects.all().delete()
        super(BaseTestCase, self).tearDown()
