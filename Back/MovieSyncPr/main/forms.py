from django.contrib.auth import get_user_model
from django.forms import ModelForm, CharField, EmailField, PasswordInput

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
