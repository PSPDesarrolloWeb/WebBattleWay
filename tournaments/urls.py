from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeAdmin),
    path('home-admin', views.homeAdmin, name='home-admin'),
    path('games/', views.gameList, name='game-list'),
    # path('create-game/', views.createGame, name='create-game'),
    path('tournaments/', views.tournamentList, name='tournament-list'),
    path('create-tournament/', views.createTournament, name='create-tournament'),
    path('edit-tournament/<int:id>', views.editTournament, name='edit-tournament'),
    path('delete-tournament/<int:id>', views.deleteTournament, name='delete-tournament'),
    path('players/', views.playersList, name='player-list'),
    # path('create-player/', views.createPlayer, name='create-player'),
    # path('edit-player/<int:id>', views.editPlayer, name='edit-player'),
    # path('delete-player/<int:id>', views.deletePlayer, name='delete-player'),
    path('points/', views.pointsView, name='points'),
    path('reports/', views.reportList, name='report-list'),
    path('ranges/', views.rangeList, name='range-list'),


] 