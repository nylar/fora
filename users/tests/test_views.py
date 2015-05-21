from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from django.test import RequestFactory
from fora.tests.base import BaseTestCase
from users.views import UserProfileView, UserRegisterView


class UserProfileViewTestCase(BaseTestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = get_user_model().objects.create(username='a', password='a')
        super(UserProfileViewTestCase, self).setUp()

    def test_get_user_profile_view(self):
        request = self.factory.get('/')
        response = UserProfileView.as_view()(
            request, username=self.user.username)
        response.render()

        self.assertEqual(response.status_code, 200)
        self.assertIn(self.user.username, response.content)


class UserRegisterViewTestCase(BaseTestCase):

    def setUp(self):
        self.factory = RequestFactory()
        super(UserRegisterViewTestCase, self).setUp()

    def test_get_user_register_view(self):
        request = self.factory.get('/')
        response = UserRegisterView.as_view()(request)
        response.render()

        self.assertEqual(response.status_code, 200)
        self.assertIn('<label for="id_username">', response.content)
        self.assertIn('<label for="id_password1">', response.content)
        self.assertIn('<label for="id_password2">', response.content)

    def test_post_user_register_view(self):
        request = self.factory.post(reverse('users:register'), data={
            'username': 'admin',
            'password1': 'secret',
            'password2': 'secret',
        })
        response = UserRegisterView.as_view()(request)

        u = get_user_model().objects.get(username='admin')

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse(
            'users:profile', kwargs={'username': u.username}))
