from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm, CharField, PasswordInput, TextInput, EmailInput


class RegisterForm(ModelForm):
    username = CharField(label='Имя')
    email = CharField(label='Email', widget=EmailInput)
    password = CharField(label='Пароль', widget=PasswordInput)
    password2 = CharField(label='Повтор пароля', widget=PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'password2']
        labels = {
            'email': 'Email',
            'username': 'Имя',
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd.get('password') != cd.get('password2'):
            raise ValidationError("Пароли не совпадают")
        return cd['password2']

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        if email and get_user_model().objects.filter(email=email).exists():
            raise ValidationError('Данный email уже занят!')
        return cleaned_data