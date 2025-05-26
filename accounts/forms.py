from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Photo

class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image']
