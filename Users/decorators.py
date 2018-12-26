from functools import wraps
from urllib.parse import urlparse

from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.core.exceptions import PermissionDenied
from django.shortcuts import resolve_url
from django.contrib.auth.decorators import user_passes_test


def user_in_group(groups):
	def decorator(func):
		@wraps(func)
		def check_perms(*args, **kwargs):
			req = args[0]
			users_groups = req.user.groups.values_list('name', flat=True)
			if len(set(users_groups).intersection(groups)) <= 0:
				raise PermissionDenied
			return func(*args, **kwargs)
		return check_perms
	return decorator

	# def check_groups(user):
	# 	for group in user.groups.values_list('name', flat=True):



	# def check_perms(user):
	# 	if isinstance(perm, str):
	# 		perms = (perm,)
	# 	else:
	# 		perms = perm
	# 	# First check if the user has the permission (even anon users)
	# 	if user.has_perms(perms):
	# 		return True
	# 	# In case the 403 handler should be called raise the exception
	# 	if raise_exception:
	# 		raise PermissionDenied
	# 	# As the last resort, show the login form
	# 	return False
	#
	# return user_passes_test(check_perms, login_url=login_url)
