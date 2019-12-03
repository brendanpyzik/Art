from django import forms
from django.contrib.auth.models import User

forms.CharField(required=True, max_length=200)


class RegistrationForm(forms.Form):
    first_name = forms.CharField(required=True, max_length=200)
    last_name = forms.CharField(required=True, max_length=200)
    email = forms.EmailField(required=True, max_length=200)
    username = forms.CharField(required=True, max_length=200)
    password = forms.CharField(required=True, max_length=200)


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
