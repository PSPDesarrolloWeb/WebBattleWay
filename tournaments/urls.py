from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeClient, name='home-client'),
    path('home-client', views.homeClient, name='home-client'),
    path('register/', views.registerAdmin, name='register'),
    path('accounts/login/?next=/home-admin', views.loginClient, name='accounts/login/?next=/home-admin'),
    path('home-admin', views.homeAdmin, name='home-admin'),
    path('logoutAdmin', views.logoutAdmin, name='logoutAdmin'),
    path('games/', views.gameList, name='game-list'),
    # path('create-game/', views.createGame, name='create-game'),
    path('tournaments/', views.tournamentList, name='tournament-list'),
    path('create-tournament/', views.createTournament, name='create-tournament'),
    path('edit-tournament/<int:id>', views.editTournament, name='edit-tournament'),
    path('delete-tournament/<int:id>', views.deleteTournament, name='delete-tournament'),
    path('players/', views.playersList, name='player-list'),
    path('updatePoints/', views.update_points, name='updatePoints'),
    # path('create-player/', views.createPlayer, name='create-player'),
    # path('edit-player/<int:id>', views.editPlayer, name='edit-player'),
    # path('delete-player/<int:id>', views.deletePlayer, name='delete-player'),
    path('points/', views.pointsView, name='points'),
    path('reports/', views.reportList, name='report-list'),
    path('ranges/', views.rangeList, name='range-list'),


] 