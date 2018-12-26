from functools import wraps
from django.core.exceptions import PermissionDenied


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
