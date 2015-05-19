import datetime

from django.utils import timezone
from fora.tests.base import BaseTestCase
from forums.models import Forum
from mock import patch
from posts.models import Post
from threads.models import Thread


class ThreadModelTestCase(BaseTestCase):

    def setUp(self):
        self.forum = Forum.objects.create(name='Test', description='Testing')
        self.thread = Thread.objects.create(
            subject='My First Thread',
            forum=self.forum,
        )
        super(ThreadModelTestCase, self).setUp()

    def test_new_thread(self):
        self.assertEqual(Thread.objects.count(), 1)
        self.assertEqual(Thread.objects.get(pk=1), self.thread)

    def test_thread_to_string(self):
        self.assertEqual(str(self.thread), "My First Thread")

    def test_thread_to_unicode(self):
        self.assertEqual(unicode(self.thread), u'My First Thread')

    @patch.object(timezone, 'now', return_value=datetime.datetime(2015, 1, 1))
    def test_thread_creation_date(self, mock_now):
        t = Thread.objects.create(subject='Mocked Date', forum=self.forum)
        self.assertEqual(t.created, datetime.datetime(2015, 1, 1))

    def test_posts_empty(self):
        posts = self.thread.posts()
        self.assertEqual(len(posts), 0)
        self.assertEqual(list(posts), [])

    def test_posts(self):
        p1 = Post.objects.create(message='p1', thread=self.thread)
        p2 = Post.objects.create(message='p2', thread=self.thread, parent=p1)

        posts = self.thread.posts()
        self.assertEqual(len(posts), 2)
        self.assertEqual(list(posts), [p1, p2])
