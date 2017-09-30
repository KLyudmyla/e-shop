from __future__ import unicode_literals

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UsernameField

UserModel = get_user_model()
from django.forms import EmailField


class LoginForm(AuthenticationForm):
    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.
    """
    username = EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'autofocus': True, 'placeholder': 'E-mail*'}),
    )
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password*'}),
    )
  #  remember = forms.BooleanField(required=False, widget=forms.CheckboxInput())

