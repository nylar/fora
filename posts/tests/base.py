from django.test import TestCase
from forums.models import Forum
from posts.models import Post
from threads.models import Thread


class BasePostTestCase(TestCase):

    def tearDown(self):
        Post.objects.all().delete()
        Thread.objects.all().delete()
        Forum.objects.all().delete()
        super(BasePostTestCase, self).tearDown()
