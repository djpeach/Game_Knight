from django.urls import reverse_lazy
from django.views import generic
from . import models
from Users import mixins as users_mixins


def index(req):
	pass


class ModGameCreate(users_mixins.GroupRequiredMixin, generic.CreateView):
	group_required = ['Moderators']

	model = models.Game
	fields = '__all__'


class ModGameList(users_mixins.GroupRequiredMixin, generic.ListView):
	group_required = ['Moderators']

	model = models.Game


class ModGameDetail(users_mixins.GroupRequiredMixin, generic.DetailView):
	group_required = ['Moderators']

	model = models.Game


class ModGameUpdate(users_mixins.GroupRequiredMixin, generic.UpdateView):
	group_required = ['Moderators']

	model = models.Game
	fields = '__all__'


class ModGameDelete(users_mixins.GroupRequiredMixin, generic.DeleteView):
	group_required = ['Moderators']

	model = models.Game
	success_url = reverse_lazy('generator:mod-game-list')


class ModDeckCreate(users_mixins.GroupRequiredMixin, generic.CreateView):
	group_required = ['Moderators']

	model = models.Deck
	fields = '__all__'


class ModDeckList(users_mixins.GroupRequiredMixin, generic.ListView):
	group_required = ['Moderators']

	model = models.Deck


class ModDeckDetail(users_mixins.GroupRequiredMixin, generic.DetailView):
	group_required = ['Moderators']

	model = models.Deck


class ModDeckUpdate(users_mixins.GroupRequiredMixin, generic.UpdateView):
	group_required = ['Moderators']

	model = models.Deck
	fields = '__all__'


class ModDeckDelete(users_mixins.GroupRequiredMixin, generic.DeleteView):
	group_required = ['Moderators']

	model = models.Deck
	success_url = reverse_lazy('generator:mod-deck-list')


class ModCardCreate(users_mixins.GroupRequiredMixin, generic.CreateView):
	group_required = ['Moderators']

	model = models.Card
	fields = '__all__'


class ModCardList(users_mixins.GroupRequiredMixin, generic.ListView):
	group_required = ['Moderators']

	model = models.Card


class ModCardDetail(users_mixins.GroupRequiredMixin, generic.DetailView):
	group_required = ['Moderators']

	model = models.Card


class ModCardUpdate(users_mixins.GroupRequiredMixin, generic.UpdateView):
	group_required = ['Moderators']

	model = models.Card
	fields = '__all__'


class ModCardDelete(users_mixins.GroupRequiredMixin, generic.DeleteView):
	group_required = ['Moderators']

	model = models.Card
	success_url = reverse_lazy('generator:mod-card-list')
