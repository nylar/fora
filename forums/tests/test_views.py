from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory
from forums.views import ForumIndexView, NewForumView, UpdateForumView
from forums.models import Forum


class ForumIndexViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        super(ForumIndexViewTestCase, self).setUp()

    def test_index_with_no_forums(self):
        request = self.factory.get('/')
        response = ForumIndexView.as_view()(request)
        response.render()

        self.assertEqual(response.status_code, 200)
        self.assertIn('No forums found', response.content)

    def test_index_with_forums(self):
        f = Forum.objects.create(name='First Forum', description='A forum')

        request = self.factory.get('/')
        response = ForumIndexView.as_view()(request)
        response.render()

        self.assertEqual(response.status_code, 200)
        self.assertIn(f.name, response.content)
        self.assertIn(f.description, response.content)


class NewForumViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        super(NewForumViewTestCase, self).setUp()

    def test_get_new_view(self):
        request = self.factory.get('/')
        response = NewForumView.as_view()(request)
        response.render()

        self.assertEqual(response.status_code, 200)
        self.assertIn('<label for="id_name">Name:</label>', response.content)
        self.assertIn(
            '<label for="id_description">Description:</label>',
            response.content
        )
        self.assertIn(
            '<label for="id_active">Active:</label>',
            response.content
        )

    def test_post_form(self):
        request = self.factory.post(reverse('forums:new'), data={
            'name': 'My Forum',
            'description': 'My forum containing my threads'
        })
        response = NewForumView.as_view()(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('forums:index'))

    def test_post_form_invalid(self):
        request = self.factory.post(reverse('forums:new'), data={})
        response = NewForumView.as_view()(request)
        response.render()

        self.assertIn(
            '<ul class="errorlist"><li>This field is required.</li></ul>',
            response.content
        )


class UpdateForumViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.forum = Forum.objects.create(
            name='Initial Forum',
            description='A starting point'
        )
        super(UpdateForumViewTestCase, self).setUp()

    def test_get_update_view(self):
        request = self.factory.get('/')
        response = UpdateForumView.as_view()(request, slug=self.forum.slug)
        response.render()

        self.assertEqual(response.status_code, 200)
        self.assertIn(
            'name="name" type="text" value="Initial Forum"',
            response.content
        )
        self.assertIn(
            'name="description" type="text" value="A starting point"',
            response.content
        )

    def test_post_form(self):
        request = self.factory.post('/', data={
            'name': 'Updated Forum',
            'description': self.forum.description
        })
        response = UpdateForumView.as_view()(request, slug=self.forum.slug)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('forums:index'))
