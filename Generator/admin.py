from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Game)
class GameAdmin(admin.ModelAdmin):
	pass


@admin.register(models.Deck)
class DeckAdmin(admin.ModelAdmin):
	pass


@admin.register(models.Card)
class CardAdmin(admin.ModelAdmin):
	pass
