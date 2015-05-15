from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from forums.models import Forum


class ForumUrlsTestCase(TestCase):

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
        f = Forum.objects.create(name='Test', description='Test')
        response = self.client.get(
            reverse('forums:update', kwargs={'slug': f.slug})
        )
        self.assertEqual(response.status_code, 200)
