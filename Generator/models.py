from django.db import models


class Game(models.Model):
	name = models.CharField(max_length=100)

	DIFFICULTIES = (
		('easy', 'Easy'),
		('medium', 'Medium'),
		('hard', 'Hard'),
	)

	difficulty = models.CharField(max_length=10, choices=DIFFICULTIES)

	def __str__(self):
		return f'{self.name} - {self.difficulty}'


class Deck(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return f'{self.name} Deck'


class Card(models.Model):
	word = models.CharField(max_length=30)
	decks = models.ManyToManyField(Deck)
	games = models.ManyToManyField(Game)

	def __str__(self):
		return f'{self.word}'