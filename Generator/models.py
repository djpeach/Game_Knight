from django.db import models
from django.urls import reverse


class Game(models.Model):

	GAMES = (
		('pict', 'Pictionary'),
		('char', 'Charades'),
		('catc', 'Catch Phrase'),
	)

	DIFFICULTIES = (
		('e', 'Easy'),
		('m', 'Medium'),
		('h', 'Hard'),
		('i', 'Impossible'),
	)

	name = models.CharField(max_length=4, choices=GAMES)
	difficulty = models.CharField(max_length=1, choices=DIFFICULTIES)

	def __str__(self):
		return f'{self.get_name_display()} - {self.get_difficulty_display()}'

	def get_absolute_url(self):
		return reverse('generator:game-detail', kwargs={'pk': self.id})

	def deck_query(self):
		return Deck.objects.filter(card__games__name__contains=self.name, card__games__difficulty=self.difficulty).distinct()

	def card_query(self):
		return Card.objects.filter(games__name__contains=self.name, games__difficulty__contains=self.difficulty)


class Deck(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return f'{self.name}'

	def card_query(self):
		return Card.objects.filter(decks__name__contains=self.name)


class Card(models.Model):
	word = models.CharField(max_length=30)
	decks = models.ManyToManyField(Deck)
	games = models.ManyToManyField(Game)

	def __str__(self):
		return f'{self.word}'