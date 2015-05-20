from django.contrib.auth import get_user_model
from django.test import RequestFactory
from fora.tests.base import BaseTestCase
from users.views import UserProfileView


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
