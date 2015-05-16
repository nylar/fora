from django.test import TestCase
from forums.models import Forum
from threads.models import Thread


class BaseThreadTestCase(TestCase):

    def tearDown(self):
        Thread.objects.all().delete()
        Forum.objects.all().delete()
        super(BaseThreadTestCase, self).tearDown()
