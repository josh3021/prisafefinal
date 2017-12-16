from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    phoneNumber = forms.CharField(min_length=10, max_length=11)

    class Meta:
        model = User
        fields = ['username', 'password', 'phoneNumber']
        widgets = {
            'username' : forms.TextInput(attrs = {'placeholder': 'Enter Username'}),
            'password' : forms.PasswordInput(attrs = {'placeholder': 'Enter Password', 'type': 'password'}),
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
