from django.urls import path
from . import mod_views


app_name = 'generator'
urlpatterns = [
	path('', mod_views.index, name='index'),
	path('games/new/', mod_views.ModGameCreate.as_view(), name='mod-game-create'),
	path('games/', mod_views.ModGameList.as_view(), name='mod-game-list'),
	path('games/<int:pk>/', mod_views.ModGameDetail.as_view(), name='mod-game-detail'),
	path('games/<int:pk>/update/', mod_views.ModGameUpdate.as_view(), name='mod-game-update'),
	path('games/<int:pk>/delete/', mod_views.ModGameDelete.as_view(), name='mod-game-delete'),
	path('decks/new/', mod_views.ModDeckCreate.as_view(), name='mod-deck-create'),
	path('decks/', mod_views.ModDeckList.as_view(), name='mod-deck-list'),
	path('decks/<int:pk>/', mod_views.ModDeckDetail.as_view(), name='mod-deck-detail'),
	path('decks/<int:pk>/update/', mod_views.ModDeckUpdate.as_view(), name='mod-deck-update'),
	path('decks/<int:pk>/delete/', mod_views.ModDeckDelete.as_view(), name='mod-deck-delete'),
	path('cards/new/', mod_views.ModCardCreate.as_view(), name='mod-card-create'),
	path('cards/', mod_views.ModCardList.as_view(), name='mod-card-list'),
	path('cards/<int:pk>/', mod_views.ModCardDetail.as_view(), name='mod-card-detail'),
	path('cards/<int:pk>/update/', mod_views.ModCardUpdate.as_view(), name='mod-card-update'),
	path('cards/<int:pk>/delete/', mod_views.ModCardDelete.as_view(), name='mod-card-delete'),
]
