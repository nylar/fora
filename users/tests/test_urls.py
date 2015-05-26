from django.core.urlresolvers import reverse
from django.test import Client
from fora.tests.base import BaseTestCase


class UserUrlsTestCase(BaseTestCase):

    def setUp(self):
        super(UserUrlsTestCase, self).setUp()
        self.client = Client()
        self.client.login(
            username=self.user.username, password=self.user.password)

    def test_user_profile_url(self):
        response = self.client.get(
            reverse('users:profile', kwargs={'username': self.user.username}))
        self.assertEqual(response.status_code, 200)

    def test_register_url(self):
        response = self.client.get(reverse('users:register'))
        self.assertEqual(response.status_code, 200)

    def test_login_url(self):
        response = self.client.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)

    def test_logout_url(self):
        self.client.login(
            username=self.user.username, password=self._password)
        response = self.client.get(reverse('users:logout'))
        self.assertEqual(response.status_code, 301)
