from django.db import models
from django.contrib.auth import models as auth_models
from Generator import models as generator_models


class GameSession(models.Model):
	owner = models.ForeignKey(auth_models.User, on_delete=models.SET_NULL, null=True)
	game = models.ForeignKey(generator_models.Game, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return f'{self.game}'
