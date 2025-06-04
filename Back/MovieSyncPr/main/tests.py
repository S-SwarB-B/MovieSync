from django.contrib.auth import get_user_model
from django.test import TestCase

from django.urls import reverse

class LoginViewTest(TestCase):
    
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='Гришаня',
            password='123456'
        )
        self.login_url = reverse('accounts:login')
    
    def test_login_success(self):
        """Тестирование успешного входа"""
        response = self.client.post(self.login_url, {
            'username': 'Гришаня',
            'password': '123456'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('main_screen'))
    
    def test_login_failure(self):
        """Тестирование неудачного входа"""
        response = self.client.post(self.login_url, {
            'username': 'Гришаня',
            'password': '4224124'
        })
        self.assertEqual(response.status_code, 200)