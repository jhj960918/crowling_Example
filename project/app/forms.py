from django import forms
from .models import CustomUser
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        help_texts = {
            'username': None,
        }
        fields = ['username', 'password', 'name','gender', 'address', 'phone_number',] 