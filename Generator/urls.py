from django.urls import path
from . import views


app_name = 'generator'
urlpatterns = [
	path('', views.index, name='index'),
	path('games/new/', views.GameCreate.as_view(), name='game-create'),
	path('games/', views.GameList.as_view(), name='game-list'),
	path('games/<int:pk>/', views.GameDetail.as_view(), name='game-detail'),
	path('games/<int:pk>/', views.GameUpdate.as_view(), name='game-update'),
	path('games/<int:pk>/', views.GameDelete.as_view(), name='game-delete'),
	path('decks/new/', views.DeckCreate.as_view(), name='deck-create'),
	path('decks/', views.DeckList.as_view(), name='deck-list'),
	path('decks/<int:pk>/', views.DeckDetail.as_view(), name='deck-detail'),
	path('decks/<int:pk>/', views.DeckUpdate.as_view(), name='deck-update'),
	path('decks/<int:pk>/', views.DeckDelete.as_view(), name='deck-delete'),
	path('cards/new/', views.CardCreate.as_view(), name='card-create'),
	path('cards/', views.CardList.as_view(), name='card-list'),
	path('cards/<int:pk>/', views.CardDetail.as_view(), name='card-detail'),
	path('cards/<int:pk>/', views.CardUpdate.as_view(), name='card-update'),
	path('cards/<int:pk>/', views.CardDelete.as_view(), name='card-delete'),
]
