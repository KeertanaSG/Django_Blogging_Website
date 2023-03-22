from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Category, Post

class CategoryModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Test Category')

    def test_category_name(self):
        self.assertEqual(str(self.category), 'Test Category')


class PostModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.category = Category.objects.create(name='Test Category')
        self.post = Post.objects.create(title='Test post', content='This is a test post', author=self.user, category=self.category)

    def test_post_title(self):
        post = Post.objects.get(id=1)
        expected_title = f'{post.title}'
        self.assertEqual(expected_title, 'Test post')

    def test_post_content(self):
        post = Post.objects.get(id=1)
        expected_content = f'{post.content}'
        self.assertEqual(expected_content, 'This is a test post')

    def test_post_author(self):
        post = Post.objects.get(id=1)
        expected_author = f'{post.author}'
        self.assertEqual(expected_author, 'testuser')

    def test_post_category(self):
        post = Post.objects.get(id=1)
        expected_category = f'{post.category}'
        self.assertEqual(expected_category, 'Test Category')

    def test_post_views(self):
        post = Post.objects.get(id=1)
        expected_views = f'{post.views}'
        self.assertEqual(expected_views, '0')

    def test_post_list_view(self):
        response = self.client.get(reverse('blog-home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test post')
