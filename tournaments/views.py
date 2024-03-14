from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse
from .models import Game, Tournament, Player
from .forms import TournamentForm, PlayerForm, AdminForm
from django.contrib.auth.models import User
from django.db.models import Case, When, Value, CharField
import firebase_admin
from firebase_admin import credentials, firestore
from firebase_admin import storage
from datetime import datetime, timedelta
import json

cred = credentials.Certificate("credentialsFirestore.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'battlewaycloud.appspot.com'
})
bucket = storage.bucket()
db=firestore.client()

def homeClient(request):
    return render(request, 'home/home-client.html')

def registerAdmin(request):
    if request.method == 'POST':
        # Extrae los datos del formulario
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        # if password1 != password2:
        #     return redirect('register')  
        user = User.objects.create_user(username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
        user = authenticate(request, username=username, password=password1)
        if user is not None:
            login(request, user)
            return homeAdmin(request)
    return render(request, 'registration/register.html')
def loginClient(request):
    return render(request, 'registration/login.html')

def homeAdmin(request):
    firestore_users = get_all_users() 
    firestore_users_json = json.dumps(firestore_users)
    return render(request, 'pages/home-admin.html', {'firestore_users_json': firestore_users_json})

def logoutAdmin(request):
    logout(request)
    return redirect('/accounts/login/?next=/home-admin')
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
    firestore_users = get_all_users() # Obtiene los datos de Firestore

    return render(request, 'players/index.html', {'players': players, 'firestore_users': firestore_users})

# def createPlayer(request):
#     formPlayer = PlayerForm(request.POST or None, request.FILES or None)
#     if formPlayer.is_valid():
#         formPlayer.save()
#         return redirect('player-list')
#     return render(request, 'players/create.html', {'formPlayer': formPlayer})

# def editPlayer(request, id):
#     player = Player.objects.get(id=id)
#     formPlayer = PlayerForm(request.POST or None, request.FILES or None, instance=player)
#     if formPlayer.is_valid() and request.POST:
#         formPlayer.save()
#         return redirect('player-list')
#     else:
#         print ("Datos no ingresados")
#     return render(request, 'players/edit.html', {'formPlayer': formPlayer})

# def deletePlayer(request, id):
#     player = Player.objects.get(id=id)
#     player.delete()
#     return redirect('player-list')
@login_required
def pointsView(request):
    games = Game.objects.all()
    for game in games:
        game.tournaments_ended = Tournament.objects.filter(game=game, status='ended')
    firestore_users = get_all_users() # Obtiene los datos de Firestore
    return render(request, 'points/index.html', {'games': games, 'firestore_users': firestore_users})

def update_points(request):
    if request.method == 'POST':
        username = request.POST.get('participant')
        score = int(request.POST.get('score'))
        
        # Buscar el usuario en Firestore
        users_ref = db.collection('user')
        user_query = users_ref.where('username', '==', username).stream()
        user_doc = None
        for user in user_query:
            user_doc = user
            break
        
        if user_doc:
            # Actualizar el campo points incrementando el valor actual
            user_ref = users_ref.document(user_doc.id)
            user_ref.update({
                'points': firestore.Increment(score)
            })
            return redirect('points')
        else:
            return redirect('error-page')
    
    return redirect('home-page')

@login_required
def gameList(request):
    games = Game.objects.all()
    return render(request, 'games/index.html', {'games': games})

@login_required
def tournamentList(request):
    games = Game.objects.all()
    for game in games:
      game.tournaments_created = Tournament.objects.filter(game=game, status='created')
      game.tournaments_online = Tournament.objects.filter(game=game, status='online')
      game.tournaments_ended = Tournament.objects.filter(game=game, status='ended')
    return render(request, 'tournaments/index.html', {'games': games})

@login_required
def createTournament(request):
    games = Game.objects.filter(status=1)
    formTournament = TournamentForm(request.POST or None, request.FILES or None)
    if formTournament.is_valid():
        tournament = formTournament.save(commit=False)
        date_str = formTournament.cleaned_data.get('date')
        time_str = formTournament.cleaned_data.get('time')

        # Combina la fecha y hora en un solo objeto datetime
        date_time = datetime.strptime(f'{date_str} {time_str}', '%Y-%m-%d %H:%M:%S')
        date_time_plus_5_hours = date_time + timedelta(hours=5)

        image = request.FILES.get('image')
        if image:
            image.seek(0)
            blob = bucket.blob(f'tournaments/{image.name}')
            blob.upload_from_file(image, content_type=image.content_type)
            original_url = blob.media_link
            modified_url = original_url.replace('storage.googleapis.com/download/storage/v1/', 'firebasestorage.googleapis.com/v0/')
        else:
            modified_url = 'imageurl.com'

        # Genera un ID único para el documento en Firestore
        tournament_id = db.collection('tournaments').document().id

        data = {
            'creator':'XxETDfQHDSB4lnLeDY0y',
            'name': tournament.name,
            'status': tournament.status,
            'game': tournament.game.UIDGame if tournament.game else None,
            'date': date_time_plus_5_hours,
            'inscribedPlayers':[],
            'players': tournament.players,
            'points': tournament.points,
            'rules': tournament.rules,
            'url': tournament.url,
            'imageURL': modified_url
        }
        # Usa el ID generado para crear el documento en Firestore
        db.collection('tournaments').document(tournament_id).set(data)

        # Actualiza el modelo Tournament en Django con el UID del documento y el valor de modified_url
        tournament.uidRegister = tournament_id
        tournament.imageURL = modified_url
        tournament.save() # Ahora guarda el torneo con los datos de Firestore

        return redirect('tournament-list')
    else:
        print('Errores de formulario', formTournament.errors,)
    return render(request, 'tournaments/create.html', {'formTournament': formTournament, 'games': games})

@login_required
def editTournament(request, id):
    tournament = Tournament.objects.get(id=id)
    games = Game.objects.filter(status=1)
    game_id = tournament.game_id # Obtener el game_id del torneo registrado
    
    # Filtrar la lista de juegos para ubicar el juego correspondiente al game_id
    game_selected = games.filter(id=game_id).first()
    
    # Obtener los juegos restantes (que no son el juego seleccionado)
    other_games = games.exclude(id=game_id)
    
    # Concatenar el juego seleccionado y los juegos restantes
    games_ordered = [game_selected] + list(other_games)
    
    formTournament = TournamentForm(request.POST or None, request.FILES or None, instance=tournament)
    if formTournament.is_valid() and request.POST:
        formTournament.save()
        date_str = formTournament.cleaned_data.get('date')
        time_str = formTournament.cleaned_data.get('time')

        # Combina la fecha y hora en un solo objeto datetime
        date_time = datetime.strptime(f'{date_str} {time_str}', '%Y-%m-%d %H:%M:%S')
        date_time_plus_5_hours = date_time + timedelta(hours=5)

        # Obtiene la referencia al documento del torneo en Firestore usando el UID almacenado
        tournament_ref = db.collection('tournaments').document(tournament.uidRegister)
        
        # Obtiene los datos actuales del documento en Firestore
        current_data = tournament_ref.get().to_dict()
        
        # Prepara los datos para actualizar en Firestore, manteniendo inscribedPlayers sin cambios
        data = {
            'creator': 'XxETDfQHDSB4lnLeDY0y',
            'name': tournament.name,
            'status': tournament.status,
            'game': tournament.game.UIDGame if tournament.game else None,
            'date': date_time_plus_5_hours,
            'inscribedPlayers': current_data.get('inscribedPlayers', []), 
            'players': tournament.players,
            'points': tournament.points,
            'rules': tournament.rules,
            'url': tournament.url,
            'imageURL': tournament.imageURL
        }
        
        # Actualiza el documento en Firestore
        tournament_ref.set(data)
        
        return redirect('tournament-list')
    else:
        print("Datos no ingresados")
    return render(request, 'tournaments/edit.html', {'formTournament': formTournament, 'games': games_ordered, 'is_edit': True})

def deleteTournament(request, id):
    tournament = Tournament.objects.get(id=id)
    tournament.delete()
    return redirect('tournament-list')


@login_required
def reportList(request):
    reports = [
        {
            'title': 'Reporte 1',
            'player_id': 1,
            'description': 'Descripción del reporte 1',
            'status': 'Pendiente',
            'image_url': 'ruta/a/la/imagen1.jpg',
            'date': '01-01-2024',
            'status': 'Pendiente',
        },
        {
            'title': 'Reporte 2',
            'player_id': 2,
            'description': 'Descripción del reporte 2',
            'status': 'Pendiente',
            'image_url': 'ruta/a/la/imagen2.jpg',
            'date': '01-01-2024',
            'status': 'Aprobado',
        },
        {
            'title': 'Reporte 3',
            'player_id': 3,
            'description': 'Descripción del reporte 3',
            'status': 'Pendiente',
            'image_url': 'ruta/a/la/imagen2.jpg',
            'date': '01-01-2024',
            'status': 'Rechazado',
        },
    ]
    return render(request, 'reports/index.html',  {'reports': reports})
@login_required
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

