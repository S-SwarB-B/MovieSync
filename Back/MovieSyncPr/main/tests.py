from django.contrib.auth import get_user_model
from django.test import TestCase, Client
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

    def test_login_failure_password(self):
        """Тестирование неудачного входа с неверным password"""
        response = self.client.post(self.login_url, {
            'username': 'Гришаня',
            'password': '4224124'
        })
        self.assertEqual(response.status_code, 200)

    def test_login_failure_username(self):
        """Тестирование неудачного входа с неверным username"""
        response = self.client.post(self.login_url, {
            'username': 'Гришаня1',
            'password': '123456'
        })
        self.assertEqual(response.status_code, 200)

    def test_login_failure_both(self):
        """Тестирование неудачного входа с неверным username и password"""
        response = self.client.post(self.login_url, {
            'username': 'Гришаня1',
            'password': '1234563123'
        })
        self.assertEqual(response.status_code, 200)


User = get_user_model()


class RegisterViewTests(TestCase):

    def test_register_success(self):
        """Успешная регистрация"""
        response = self.client.post(reverse('accounts:register'), {
            'username': 'test1',
            'email': 'test@test.com',
            'password': '123',
            'password2': '123',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register_done.html')

        user = User.objects.get(username='test1')
        self.assertIsNotNone(user)
        self.assertEqual(user.email, 'test@test.com')
        self.assertTrue(user.check_password('123'))

    def test_register_password_mismatch(self):
        """Пароли не совпадают"""
        response = self.client.post(reverse('accounts:register'), {
            'username': 'test2',
            'email': 'test2@test.com',
            'password': '123',
            'password2': '1234',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')
        self.assertContains(response, 'Пароли не совпадают')
        self.assertFalse(User.objects.filter(username='test2').exists())

    def test_register_duplicate_username(self):
        """Регистрация с уже существующим юзернеймом"""
        User.objects.create_user(username='test3', email='existing@test.com', password='123')

        response = self.client.post(reverse('accounts:register'), {
            'username': 'test3',
            'email': 'new@test.com',
            'password': '123',
            'password2': '123',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')
        self.assertContains(response, 'Пользователь с таким именем уже существует.')
        self.assertFalse(User.objects.filter(email='test3').exists())

    def test_register_duplicate_email(self):
        """Регистрация с уже существующим емейлом"""
        User.objects.create_user(username='test4', email='existing@test.com', password='123')

        response = self.client.post(reverse('accounts:register'), {
            'username': 'test4.1',
            'email': 'existing@test.com',
            'password': '123',
            'password2': '123',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')
        self.assertContains(response, 'Пользователь с таким email уже существует.')
        self.assertFalse(User.objects.filter(email='test4').exists())

    def test_register_invalid_email(self):
        """Регистрация с некорректным емейлом"""
        response = self.client.post(reverse('accounts:register'), {
            'username': 'test5',
            'email': 'email',
            'password': '123',
            'password2': '123',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')
        self.assertContains(response, 'Введите правильный адрес электронной почты')

    def test_register_empty_fields(self):
        """Регистрация с пустыми полями"""
        response = self.client.post(reverse('accounts:register'), {
            'username': '',
            'email': '',
            'password': '',
            'password2': '',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')
        self.assertContains(response, 'Обязательное поле', count=4)



class ProfileViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = get_user_model().objects.create_user(username='user1', password='testpass123')
        self.user2 = get_user_model().objects.create_user(username='user2', password='testpass456')
        self.profile_url = lambda user_id: reverse('profile', args=[user_id])

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(self.profile_url(self.user1.id))
        self.assertRedirects(response, '/accounts/login/?next=' + self.profile_url(self.user1.id))

    def test_view_own_profile(self):
        self.client.login(username='user1', password='testpass123')
        response = self.client.get(self.profile_url(self.user1.id))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'form')  # предполагается, что шаблон содержит форму

    def test_redirect_to_own_profile_if_accessing_another(self):
        self.client.login(username='user1', password='testpass123')
        response = self.client.get(self.profile_url(self.user2.id))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'form')  # всё равно видим свою форму
        self.assertEqual(response.context['profile'].id, self.user1.id)

    def test_profile_update_post(self):
        self.client.login(username='user1', password='testpass123')
        response = self.client.post(self.profile_url(self.user1.id), {
            'username': 'newusername',
            'email': 'newemail@example.com',
            # если UpdateUserForm требует другие поля — добавь их
        }, follow=True)  # <--- Это важно
        self.assertEqual(response.status_code, 200)
        self.user1.refresh_from_db()
        self.assertEqual(self.user1.username, 'newusername')
        self.assertEqual(self.user1.email, 'newemail@example.com')