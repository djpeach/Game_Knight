from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy


class GroupRequiredMixin(UserPassesTestMixin):

	login_url = reverse_lazy('users:login')

	group_required = None

	def test_func(self):
		if not self.request.user.is_authenticated:
			return False
		else:
			user_groups = []
			for group in self.request.user.groups.values_list('name', flat=True):
				user_groups.append(group)
			if len(set(user_groups).intersection(self.group_required)) <= 0:
				return False
			return True

	def get_test_func(self):
		return self.test_func

	def dispatch(self, request, *args, **kwargs):
		if not self.group_required:
			raise NotImplementedError(
				'{0} is missing a declaration of the group_required array.'.format(self.__class__.__name__)
			)
		user_test_result = self.get_test_func()()
		if not user_test_result:
			return self.handle_no_permission()
		return super().dispatch(request, *args, **kwargs)
