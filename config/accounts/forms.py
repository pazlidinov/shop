from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from.models import Contact


class RegisterForm(UserCreationForm):
    # Login form for django standart user model

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={"class": "form-control", 'placeholder': 'example@email.com'}),
            'password1': forms.PasswordInput(attrs={"class": "form-control"}),
            'password2': forms.PasswordInput(attrs={"class": "form-control"}),
        }

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['subject', 'message']
        widgets = {

            'subject': forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={"class": "form-control", 'placeholder': 'Message', 'rows': '8'}),
        }
