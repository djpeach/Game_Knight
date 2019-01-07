from functools import wraps
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy


def user_in_group(groups):
	def decorator(func):
		@wraps(func)
		def check_perms(*args, **kwargs):
			req = args[0]
			users_groups = req.user.groups.values_list('name', flat=True)
			if len(set(users_groups).intersection(groups)) <= 0:
				messages.warning(req, f'This page requires you to be in one of the following groups: {", ".join(groups)}. Login with an account in one of these groups to access the page.')
				redirect_url = reverse_lazy('users:login')
				return redirect(f'{redirect_url}?next={req.path}')
			return func(*args, **kwargs)
		return check_perms
	return decorator
