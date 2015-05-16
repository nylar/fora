import datetime

from .base import BaseThreadTestCase
from django.utils import timezone
from forums.models import Forum
from mock import patch
from threads.models import Thread


class ThreadModelTestCase(BaseThreadTestCase):

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
