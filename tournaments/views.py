from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Game, Tournament, Player
from .forms import TournamentForm, PlayerForm
# Create your views here.
from django.db.models import Case, When, Value, CharField
import firebase_admin
from firebase_admin import credentials, firestore
from django.contrib.auth.decorators import login_required



cred = credentials.Certificate("credentialsFirestore.json")
firebase_admin.initialize_app(cred)

db=firestore.client()
@login_required
def homeAdmin(request):
    return render(request, 'pages/home-admin.html')
@login_required
def gameList(request):
    games = Game.objects.all()
    return render(request, 'games/index.html', {'games': games})

def tournamentList(request):
    games = Game.objects.all()
    for game in games:
      game.tournaments_created = Tournament.objects.filter(game=game, status='C')
      game.tournaments_online = Tournament.objects.filter(game=game, status='O')
      game.tournaments_ended = Tournament.objects.filter(game=game, status='E')
    return render(request, 'tournaments/index.html', {'games': games})

def createTournament(request):
    games = Game.objects.all()
    formTournament = TournamentForm(request.POST or None, request.FILES or None)
    if formTournament.is_valid():
        formTournament.save()
        return redirect('tournament-list')
    return render(request, 'tournaments/create.html', {'formTournament': formTournament, 'games': games },)

def editTournament(request, id):
    tournament = Tournament.objects.get(id=id)
    formTournament = TournamentForm(request.POST or None, request.FILES or None, instance=tournament)
    print (formTournament)
    if formTournament.is_valid() and request.POST:
        formTournament.save()
        return redirect('tournament-list')
    else:
        print ("Datos no ingresados")
    return render(request, 'tournaments/edit.html', {'formTournament': formTournament, 'is_edit': True})

def deleteTournament(request, id):
    tournament = Tournament.objects.get(id=id)
    tournament.delete()
    return redirect('tournament-list')

def get_all_users():
    users_ref = db.collection('user')
    users = users_ref.stream()
    users_data = []
    for user in users:
        users_data.append(user.to_dict())
    return users_data

def playersList(request):
    players = Player.objects.all()
    print(players)
    print (get_all_users())
    return render(request, 'players/index.html', {'players': players})

def createPlayer(request):
    formPlayer = PlayerForm(request.POST or None, request.FILES or None)
    if formPlayer.is_valid():
        formPlayer.save()
        return redirect('player-list')
    return render(request, 'players/create.html', {'formPlayer': formPlayer})

def editPlayer(request, id):
    player = Player.objects.get(id=id)
    formPlayer = PlayerForm(request.POST or None, request.FILES or None, instance=player)
    if formPlayer.is_valid() and request.POST:
        formPlayer.save()
        return redirect('player-list')
    else:
        print ("Datos no ingresados")
    return render(request, 'players/edit.html', {'formPlayer': formPlayer})

def deletePlayer(request, id):
    player = Player.objects.get(id=id)
    player.delete()
    return redirect('player-list')

def reportList(request):
    reports = [
        {
            'title': 'Reporte 1',
            'player_id': 1,
            'description': 'Descripción del reporte 1',
            'status': 'Pendiente',
            'image_url': 'ruta/a/la/imagen1.jpg'
        },
        {
            'title': 'Reporte 2',
            'player_id': 2,
            'description': 'Descripción del reporte 2',
            'status': 'Pendiente',
            'image_url': 'ruta/a/la/imagen2.jpg'
        },
        {
            'title': 'Reporte 3',
            'player_id': 3,
            'description': 'Descripción del reporte 3',
            'status': 'Pendiente',
            'image_url': 'ruta/a/la/imagen2.jpg'
        },
    ]
    return render(request, 'reports/index.html',  {'reports': reports})
def rangeList(request):
    ranges = [
        {
            'nombre': 'Novato',
            'detalle': '¡Bienvenido al mundo de Battle Way! Comienza tu viaje y demuestra tu valía.',
            'img': 'https://cdn.ligadegamers.com/imagenes/novato-1-cod-mobile-mj-1.jpg'
            # 'rango_puntajes': (0, puntaje_tope * 0.25),
        },
        {
            'nombre': 'Amateur',
            'detalle': 'Has ganado algunas batallas. Sigue mejorando para alcanzar nuevos logros.',
            'img': 'https://cdn.ligadegamers.com/imagenes/lite-1-cod-mobile-mj.jpg'
            # 'rango_puntajes': (puntaje_tope * 0.26, puntaje_tope * 0.5),
        },
        {
            'nombre': 'Experto',
            'detalle': 'Eres un jugador experimentado. Desafía a otros expertos y demuestra tu maestría.',
            'img': 'https://cdn.ligadegamers.com/imagenes/profesional-1-cod-mobile-mj.jpg'
            # 'rango_puntajes': (puntaje_tope * 0.51, puntaje_tope * 0.75),
        },
        {
            'nombre': 'Maestro',
            'detalle': 'Solo unos pocos han llegado tan lejos. Tu destreza es reconocida en todo el campo de batalla.',
            'img': 'https://cdn.ligadegamers.com/imagenes/maestro-1-cod-mobile-mj-0.jpg'
            # 'rango_puntajes': (puntaje_tope * 0.76, puntaje_tope * 0.9),
        },
        {
            'nombre': 'Leyenda',
            'detalle': 'Eres una leyenda viva en Battle Way. Tu nombre resuena en cada rincón del juego.',
            'img': 'https://cdn.ligadegamers.com/imagenes/legendario-mejores-5000-cod-mobile-mj.jpg'
            # 'rango_puntajes': (puntaje_tope * 0.91, float('inf')),
        },
    ]
    return render(request, 'ranges/index.html', {'ranges': ranges})

