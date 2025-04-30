<<<<<<< HEAD
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class BlogPageTemplateTest(TestCase):
    def setUp(self) -> None:
        # Create a user and log them in before each test
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_page_template_used(self) -> None:
        response = self.client.get(reverse('blog'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog.html')
=======
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class BlogPageTemplateTest(TestCase):
    def setUp(self) -> None:
        # Create a user and log them in before each test
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_page_template_used(self) -> None:
        response = self.client.get(reverse('blog'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog.html')
>>>>>>> 49c1d749563c4b264d06f2cf3418138d200a600b
