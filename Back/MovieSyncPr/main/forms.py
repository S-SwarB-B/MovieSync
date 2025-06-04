from django.contrib.auth import get_user_model
from django.forms import ModelForm, CharField, EmailField, PasswordInput
from django.contrib.auth.hashers import make_password

class UpdateUserForm(ModelForm):
    username = CharField(required=True)
    email = EmailField(required=True)
    password = CharField(
        required=False,
        widget=PasswordInput(render_value=True)
    )

    class Meta:
        model = get_user_model()
        fields = ['username','email', 'password']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')

        if password:
            user.password = make_password(password)
        
        if commit:
            user.save()

        return user
