from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth import models as auth_models
from . import models, mixins


def index(req):
	pass


class ModGameCreate(mixins.GroupRequiredMixin, generic.CreateView):
	group_required = ['Moderators']

	model = models.Game
	fields = '__all__'


class ModGameList(mixins.GroupRequiredMixin, generic.ListView):
	group_required = ['Moderators']

	model = models.Game


class ModGameDetail(mixins.GroupRequiredMixin, generic.DetailView):
	group_required = ['Moderators']

	model = models.Game


class ModGameUpdate(mixins.GroupRequiredMixin, generic.UpdateView):
	group_required = ['Moderators']

	model = models.Game
	fields = '__all__'


class ModGameDelete(mixins.GroupRequiredMixin, generic.DeleteView):
	group_required = ['Moderators']

	model = models.Game
	success_url = reverse_lazy('generator:mod-game-list')


class ModDeckCreate(mixins.GroupRequiredMixin, generic.CreateView):
	group_required = ['Moderators']

	model = models.Deck
	fields = '__all__'


class ModDeckList(mixins.GroupRequiredMixin, generic.ListView):
	group_required = ['Moderators']

	model = models.Deck


class ModDeckDetail(mixins.GroupRequiredMixin, generic.DetailView):
	group_required = ['Moderators']

	model = models.Deck


class ModDeckUpdate(mixins.GroupRequiredMixin, generic.UpdateView):
	group_required = ['Moderators']

	model = models.Deck
	fields = '__all__'


class ModDeckDelete(mixins.GroupRequiredMixin, generic.DeleteView):
	group_required = ['Moderators']

	model = models.Deck
	success_url = reverse_lazy('generator:mod-deck-list')


class ModCardCreate(mixins.GroupRequiredMixin, generic.CreateView):
	group_required = ['Moderators']

	model = models.Card
	fields = '__all__'


class ModCardList(mixins.GroupRequiredMixin, generic.ListView):
	group_required = ['Moderators']

	model = models.Card


class ModCardDetail(mixins.GroupRequiredMixin, generic.DetailView):
	group_required = ['Moderators']

	model = models.Card


class ModCardUpdate(mixins.GroupRequiredMixin, generic.UpdateView):
	group_required = ['Moderators']

	model = models.Card
	fields = '__all__'


class ModCardDelete(mixins.GroupRequiredMixin, generic.DeleteView):
	group_required = ['Moderators']

	model = models.Card
	success_url = reverse_lazy('generator:mod-card-list')
