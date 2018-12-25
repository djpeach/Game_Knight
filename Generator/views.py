from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth import models as auth_models
from . import models, mixins


def index(req):
	pass


class GameCreate(mixins.GroupRequiredMixin, generic.CreateView):
	group_required = ['Moderators']

	model = models.Game
	fields = '__all__'


class GameList(mixins.GroupRequiredMixin, generic.ListView):
	group_required = ['Moderators']

	model = models.Game


class GameDetail(mixins.GroupRequiredMixin, generic.DetailView):
	group_required = ['Moderators']

	model = models.Game


class GameUpdate(mixins.GroupRequiredMixin, generic.UpdateView):
	groups_required = ['Moderators']

	model = models.Game
	fields = '__all__'


class GameDelete(mixins.GroupRequiredMixin, generic.DeleteView):
	group_required = ['Moderators']

	model = models.Game
	success_url = reverse_lazy('generator:game-list')


class DeckCreate(mixins.GroupRequiredMixin, generic.CreateView):
	group_required = ['Moderators']

	model = models.Deck
	fields = '__all__'


class DeckList(mixins.GroupRequiredMixin, generic.ListView):
	group_required = ['Moderators']

	model = models.Deck


class DeckDetail(mixins.GroupRequiredMixin, generic.DetailView):
	group_required = ['Moderators']

	model = models.Deck


class DeckUpdate(mixins.GroupRequiredMixin, generic.UpdateView):
	groups_required = ['Moderators']

	model = models.Deck
	fields = '__all__'


class DeckDelete(mixins.GroupRequiredMixin, generic.DeleteView):
	group_required = ['Moderators']

	model = models.Deck
	success_url = reverse_lazy('generator:deck-list')


class CardCreate(mixins.GroupRequiredMixin, generic.CreateView):
	group_required = ['Moderators']

	model = models.Card
	fields = '__all__'


class CardList(mixins.GroupRequiredMixin, generic.ListView):
	group_required = ['Moderators']

	model = models.Card


class CardDetail(mixins.GroupRequiredMixin, generic.DetailView):
	group_required = ['Moderators']

	model = models.Card


class CardUpdate(mixins.GroupRequiredMixin, generic.UpdateView):
	groups_required = ['Moderators']

	model = models.Card
	fields = '__all__'


class CardDelete(mixins.GroupRequiredMixin, generic.DeleteView):
	group_required = ['Moderators']

	model = models.Card
	success_url = reverse_lazy('generator:card-list')
