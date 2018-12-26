from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import decorators as auth_decorators
from . import forms
from . import decorators


def user_registration(req):
	if req.method == 'POST':
		form = forms.UserRegistrationForm(req.POST)
		if form.is_valid():
			form.save()
			messages.success(req, "Your account has been successfully created, go ahead and log in!")
			return redirect('users:login')
	else:
		form = forms.UserRegistrationForm()

	return render(req, 'users/user_form.html', {'form': form})


@auth_decorators.login_required(login_url=reverse_lazy('users:login'))
def user_profile(req):
	return render(req, 'users/profile.html')
