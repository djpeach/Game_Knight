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
]
