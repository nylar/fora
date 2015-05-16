from forums.models import Forum
from .base import BaseForumTestCase


class ForumModelTestCase(BaseForumTestCase):

    def setUp(self):
        self.forum = Forum.objects.create(
            name='Test',
            description='Forum for testing'
        )
        super(ForumModelTestCase, self).setUp()

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

    def test_only_visible_forums(self):
        for i in xrange(1, 4):
            Forum.objects.create(name='%d' % i, active=True)

        # 3 active, 1 inactive
        self.assertEqual(Forum.objects.count(), 4)
        self.assertEqual(Forum.visible.count(), 3)

        # 'Test' forum should not be in visible forums
        self.assertNotIn(self.forum, Forum.visible.all())
