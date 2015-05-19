from fora.tests.base import BaseTestCase
from forums.models import Forum
from threads.models import Thread


class ForumModelTestCase(BaseTestCase):

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

    def test_threads_empty(self):
        threads = self.forum.threads()
        self.assertEqual(len(threads), 0)
        self.assertEqual(list(threads), [])

    def test_threads(self):
        t1 = Thread.objects.create(subject='t1', forum=self.forum)
        t2 = Thread.objects.create(subject='t2', forum=self.forum)

        threads = self.forum.threads()
        self.assertEqual(len(threads), 2)
        self.assertEqual(list(threads), [t1, t2])
