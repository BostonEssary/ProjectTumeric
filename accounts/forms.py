from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import MyUser

class LoginForm(AuthenticationForm):
    pass 

class AvatarForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = (
            'avatar',
        )