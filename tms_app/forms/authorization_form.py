from django.forms import ModelForm
from django import forms
from django.contrib.auth import authenticate


class AuthorizationForm(forms.Form):
    """Форма авторизации"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


