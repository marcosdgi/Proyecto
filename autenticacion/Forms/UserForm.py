
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class Usuario(UserCreationForm):
    email = forms.EmailField()
    class Meta():
        model = User
        fields = [
            'username','email'
        ]
        widgets = {
            'username':forms.TextInput(),
            'password':forms.PasswordInput(),
            'Confirm password':forms.PasswordInput(),
            'email':forms.EmailInput()
        }