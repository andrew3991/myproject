from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms

class LoginForm(AuthenticationForm):
	username = forms.CharField(label="Username", max_length=30, 
		widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))

	password = forms.CharField(label="Password", max_length=30, 
		widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))

