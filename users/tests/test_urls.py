from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import Client
from fora.tests.base import BaseTestCase


class UserUrlsTestCase(BaseTestCase):

    def setUp(self):
        super(UserUrlsTestCase, self).setUp()
        self.client = Client()

    def test_user_profile_url(self):
        u = get_user_model().objects.create(username='u', password='x')
        response = self.client.get(
            reverse('users:profile', kwargs={'username': u.username}))
        self.assertEqual(response.status_code, 200)

    def test_register_url(self):
        response = self.client.get(reverse('users:register'))
        self.assertEqual(response.status_code, 200)
