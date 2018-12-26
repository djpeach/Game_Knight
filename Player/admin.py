from django.contrib import admin
from . import models


@admin.register(models.GameSession)
class GameSessionAdmin(admin.ModelAdmin):
	pass
