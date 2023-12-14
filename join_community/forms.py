# join_community/forms.py
from django import forms
from .models import UserProfile


class SignUpForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password']

        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
        }


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['subscription']
