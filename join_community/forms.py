# join_community/forms.py
from django import forms
from .models import UserProfile


class SignUpForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'email']


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['subscription']
