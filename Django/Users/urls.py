from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
	path('register/', views.user_registration, name='registration'),
	path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(template_name='auth/logout.html'), name='logout'),
	path('profile/', views.user_profile, name='profile'),
]