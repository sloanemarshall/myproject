from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
        last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
        email = forms.CharField(max_length=150, required=True, help_text='Required.')
        fields = ('username', 'first_name', 'last_name','birth_date', 'email', 'password1', 'password2', )# -*- coding: utf-8 -*-
