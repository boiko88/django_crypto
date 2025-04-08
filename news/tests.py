from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class NewsPageTemplateTest(TestCase):
    def setUp(self):
        # Create a user and log them in before each test
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_page_template_used(self):
        response = self.client.get(reverse('news'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news.html')
