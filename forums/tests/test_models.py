from django.test import TestCase
from forums.models import Forum


class ForumModelTestCase(TestCase):

    def setUp(self):
        self.forum = Forum.objects.create(
            name='Test',
            description='Forum for testing'
        )
        super(ForumModelTestCase, self).setUp()

    def tearDown(self):
        self.forum.delete()
        super(ForumModelTestCase, self).tearDown()

    def test_new_forum(self):
        self.assertEqual(Forum.objects.count(), 1)
        self.assertEqual(Forum.objects.get(pk=1), self.forum)

    def test_forum_to_string(self):
        self.assertEqual(str(self.forum), "Test")

    def test_forum_to_unicode(self):
        self.assertEqual(unicode(self.forum), u'Test')

    def test_forum_generates_slug(self):
        self.assertEqual(self.forum.slug, 'test')

    def test_forum_updates_slug(self):
        self.assertEqual(self.forum.slug, 'test')

        self.forum.name = 'Updated Test'
        self.forum.save()
        self.assertEqual(self.forum.slug, 'updated-test')
