from django import forms as f
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = f.CharField(widget=f.TextInput(
        attrs={'class': 'form-control form-control-lg', 'placeholder': 'Username', 'required': True,
               'autofocus': True}))
    password = f.CharField(
        widget=f.PasswordInput(
            attrs={'class': 'form-control form-control-lg', 'placeholder': 'Password', 'required': True})),
    remember_me = f.BooleanField(required=False)