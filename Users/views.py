from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
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

	return render(req, 'auth/user_form.html', {'form': form})


@decorators.user_in_group(groups=['Moderators'])
def user_profile(req):
	return HttpResponse('hey')
