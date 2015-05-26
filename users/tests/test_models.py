from django.contrib.auth import get_user_model
from fora.tests.base import BaseTestCase


class UserModelTestCase(BaseTestCase):

    def setUp(self):
        super(UserModelTestCase, self).setUp()

    def test_new_user(self):
        self.assertEqual(get_user_model().objects.count(), 1)
        self.assertEqual(get_user_model().objects.get(pk=1), self.user)

    def test_user_to_string(self):
        self.assertEqual(str(self.user), "user")

    def test_user_to_unicode(self):
        self.assertEqual(unicode(self.user), u'user')
