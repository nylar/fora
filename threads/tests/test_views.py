from .base import BaseThreadTestCase
from django.core.urlresolvers import reverse
from django.test import RequestFactory
from forums.models import Forum
from threads.models import Thread
from threads.views import NewThreadView, ShowThreadView


class NewThreadViewTestCase(BaseThreadTestCase):

    def setUp(self):
        self.factory = RequestFactory()
        super(NewThreadViewTestCase, self).setUp()

    def test_get_new_view(self):
        request = self.factory.get('/')
        response = NewThreadView.as_view()(request)
        response.render()

        self.assertEqual(response.status_code, 200)
        self.assertIn(
            '<label for="id_subject">Subject:</label>',
            response.content
        )
        self.assertIn(
            '<label for="id_forum">Forum:</label>',
            response.content
        )

    def test_post_form(self):
        forum = Forum.objects.create(name='My Forum', description='Hello World')
        request = self.factory.post(reverse('threads:new'), data={
            'subject': 'My thread',
            'forum': forum.pk
        })
        response = NewThreadView.as_view()(request)

        thread = Thread.objects.get(pk=1)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse(
            'threads:show', kwargs={'slug': thread.slug}))


class ShowThreadViewTestCase(BaseThreadTestCase):

    def setUp(self):
        self.factory = RequestFactory()
        super(ShowThreadViewTestCase, self).setUp()

    def test_show_view(self):
        forum = Forum.objects.create(
            name='Forum',
            description='A forum',
            active=True,
        )
        thread = Thread.objects.create(subject='Thread', forum=forum)

        request = self.factory.get('/')
        response = ShowThreadView.as_view()(request, slug=thread.slug)
        response.render()

        self.assertEqual(response.status_code, 200)
        self.assertIn(thread.subject, response.content)
