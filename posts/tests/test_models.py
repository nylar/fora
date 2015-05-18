import datetime

from django.utils import timezone
from forums.models import Forum
from mock import patch
from posts.models import Post
from threads.models import Thread
from .base import BasePostTestCase


class PostModelTestCase(BasePostTestCase):

    def setUp(self):
        self.forum = Forum.objects.create(name='Forum', description='Testing')
        self.thread = Thread.objects.create(subject='Thread', forum=self.forum)
        self.post = Post.objects.create(
            message='Post', thread=self.thread, parent=None)
        super(PostModelTestCase, self).setUp()

    def test_new_post(self):
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get(pk=1), self.post)

    def test_post_to_string(self):
        self.assertEqual(str(self.post), "o4")

    def test_post_to_unicode(self):
        self.assertEqual(unicode(self.post), u'o4')

    @patch.object(timezone, 'now', return_value=datetime.datetime(2015, 1, 1))
    def test_thread_created_date_and_updated_date(self, mock_now):
        p = Post.objects.create(
            message='Post', thread=self.thread, parent=None)
        self.assertEqual(p.created, datetime.datetime(2015, 1, 1))
        self.assertEqual(p.updated, datetime.datetime(2015, 1, 1))
