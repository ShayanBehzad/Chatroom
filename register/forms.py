from dataclasses import fields
from django import forms
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import CharField, ModelForm
from django.core.validators import RegexValidator
from main.models import *
from register.models import User


class Registerform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'password1', 'password2']


class Logginform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
