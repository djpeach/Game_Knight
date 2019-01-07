from django.contrib.auth import forms as auth_forms
from django.contrib.auth.models import User
from django import forms


class UserRegistrationForm(auth_forms.UserCreationForm):
	# email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
