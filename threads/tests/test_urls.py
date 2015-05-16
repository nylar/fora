from django.core.urlresolvers import reverse
from django.test import Client
from forums.models import Forum
from threads.models import Thread
from .base import BaseThreadTestCase


class ThreadUrlsTestCase(BaseThreadTestCase):

    def setUp(self):
        super(ThreadUrlsTestCase, self).setUp()
        self.client = Client()

    def test_new_url(self):
        response = self.client.get(reverse('threads:new'))
        self.assertEqual(response.status_code, 200)

    def test_show_url(self):
        forum = Forum.objects.create(
            name='Forum',
            description='A forum',
            active=True,
        )
        thread = Thread.objects.create(subject='Thread', forum=forum)

        response = self.client.get(reverse(
            'threads:show', kwargs={'slug': thread.slug}))
        self.assertEqual(response.status_code, 200)

    def test_show_url_not_valid(self):
        response = self.client.get(reverse(
            'threads:show', kwargs={'slug': 'does-not-exist'}))
        self.assertEqual(response.status_code, 404)
