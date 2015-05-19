from django.core.urlresolvers import reverse
from django.test import Client
from fora.tests.base import BaseTestCase
from forums.models import Forum


class ForumUrlsTestCase(BaseTestCase):

    def setUp(self):
        super(ForumUrlsTestCase, self).setUp()
        self.client = Client()

    def test_index_url(self):
        response = self.client.get(reverse('forums:index'))
        self.assertEqual(response.status_code, 200)

    def test_new_url(self):
        response = self.client.get(reverse('forums:new'))
        self.assertEqual(response.status_code, 200)

    def test_update_url(self):
        f = Forum.objects.create(name='Test', description='Test', active=True)
        response = self.client.get(
            reverse('forums:update', kwargs={'slug': f.slug})
        )
        self.assertEqual(response.status_code, 200)

    def test_update_url_not_found(self):
        f = Forum.objects.create(name='Test', description='Test', active=False)
        response = self.client.get(
            reverse('forums:update', kwargs={'slug': f.slug})
        )
        self.assertEqual(response.status_code, 404)

    def test_visibility_url(self):
        f = Forum.objects.create(
            name='Visible',
            description='I am visible',
            active=True
        )
        response = self.client.get(
            reverse('forums:visibility', kwargs={'slug': f.slug})
        )
        self.assertEqual(response.status_code, 200)

    def test_show_url(self):
        f = Forum.objects.create(name='Test', description='Test', active=True)
        response = self.client.get(
            reverse('forums:show', kwargs={'slug': f.slug})
        )
        self.assertEqual(response.status_code, 200)

    def test_show_url_not_found(self):
        f = Forum.objects.create(name='Test', description='Test', active=False)
        response = self.client.get(
            reverse('forums:show', kwargs={'slug': f.slug})
        )
        self.assertEqual(response.status_code, 404)
