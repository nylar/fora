from django.test import TestCase
from forums.models import Forum


class BaseForumTestCase(TestCase):

    def tearDown(self):
        Forum.objects.all().delete()
        super(BaseForumTestCase, self).tearDown()
