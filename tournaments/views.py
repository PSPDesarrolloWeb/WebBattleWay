from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, JsonResponse
from .models import Game, Tournament, Player
from .forms import TournamentForm, PlayerForm, AdminForm
from django.contrib.auth.models import User
from django.db.models import Case, When, Value, CharField
import firebase_admin
from firebase_admin import credentials, firestore
from firebase_admin import storage
from datetime import datetime, timedelta
import json
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO

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
        user_data = user.to_dict()
        user_data['uid'] = user.id 
        users_data.append(user_data)
    return users_data

def playersList(request):
    if request.method == 'POST':
        filtered_data = request.POST.getlist('filteredRows[]')
        print(filtered_data)
        return JsonResponse({'success': True})

    players = Player.objects.all()
    firestore_users = get_all_users()

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
        ended_tournaments = Tournament.objects.filter(game=game, status='ended')
        game.tournaments_ended = []
        
        for tournament in ended_tournaments:
            firestore_tournament = db.collection('tournaments').document(tournament.uidRegister).get().to_dict()
            if firestore_tournament:
                tournament.inscribedPlayers = firestore_tournament.get('inscribedPlayers', [])
            game.tournaments_ended.append(tournament)

    firestore_users = get_all_users()
    return render(request, 'points/index.html', {'games': games, 'firestore_users': firestore_users})

from firebase_admin import firestore

def update_points(request):
    if request.method == 'POST':
        gameId = request.POST.get('gameId')
        gameName = request.POST.get('gameName')
        tournamentId = request.POST.get('tournamentId')
        tournamentName = request.POST.get('tournamentName')
        
        points_data = []

        descriptions = request.POST.getlist('description')
        participants = request.POST.getlist('participant')
        scores = request.POST.getlist('score')

        for i in range(len(descriptions)):
            description = descriptions[i]
            participant = participants[i]
            score = int(scores[i])

            users_ref = db.collection('user')
            user_query = users_ref.where('username', '==', participant).stream()
            user_doc = None

            for user in user_query:
                user_doc = user
                break

            if user_doc:
                user_ref = users_ref.document(user_doc.id)
                user_ref.update({
                    'points': firestore.Increment(score)
                })

                points_data.append({
                    'userId': user_doc.id,
                    'points': score,
                    'gameId': gameId,
                    'gameName': gameName,
                    'tournamentId': tournamentId,
                    'tournamentName': tournamentName,
                    'description': description,
                    'timestamp': firestore.SERVER_TIMESTAMP
                })
            else:
                return redirect('error-page')

        points_history_ref = db.collection('pointsHistory')
        for data in points_data:
            points_history_ref.add(data)

        return redirect('points')

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

        # # Procesar los torneos creados
        # created_tournaments = Tournament.objects.filter(game=game, status='created')
        # for tournament in created_tournaments:
        #     firestore_tournament = db.collection('tournaments').document(tournament.uidRegister).get().to_dict()
        #     if firestore_tournament:
        #         tournament.inscribedPlayers = firestore_tournament.get('inscribedPlayers', [])
        #     else:
        #         game.tournaments_created.append(tournament)

        # # Procesar los torneos en línea
        # online_tournaments = Tournament.objects.filter(game=game, status='online')
        # for tournament in online_tournaments:
        #     firestore_tournament = db.collection('tournaments').document(tournament.uidRegister).get().to_dict()
        #     if firestore_tournament:
        #         tournament.inscribedPlayers = firestore_tournament.get('inscribedPlayers', [])
        #     else:
        #         game.tournaments_online.append(tournament)

        # Procesar los torneos finalizados
        ended_tournaments = Tournament.objects.filter(game=game, status='ended')
        for tournament in ended_tournaments:
            firestore_tournament = db.collection('tournaments').document(tournament.uidRegister).get().to_dict()
            if firestore_tournament:
                tournament.inscribedPlayers = firestore_tournament.get('inscribedPlayers', [])
            else:
                game.tournaments_ended.append(tournament)

    return render(request, 'tournaments/index.html', {'games': games})

@login_required
def createTournament(request):
    games = Game.objects.filter(status=1)
    formTournament = TournamentForm(request.POST or None, request.FILES or None)
    if formTournament.is_valid():
        tournament = formTournament.save(commit=False)
        date_str = formTournament.cleaned_data.get('date')
        time_str = formTournament.cleaned_data.get('time')

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
            'avalaiblePoints': tournament.points,
            'rules': tournament.rules,
            'url': tournament.url,
            'imageURL': modified_url
        }
        db.collection('tournaments').document(tournament_id).set(data)

        tournament.avalaible_points = tournament.points
        tournament.uidRegister = tournament_id
        tournament.imageURL = modified_url
        tournament.save()

        return redirect('tournament-list')
    else:
        print('Errores de formulario', formTournament.errors,)
    return render(request, 'tournaments/create.html', {'formTournament': formTournament, 'games': games})

@login_required
def editTournament(request, id):
    tournament = Tournament.objects.get(id=id)
    games = Game.objects.filter(status=1)
    game_id = tournament.game_id
    
    game_selected = games.filter(id=game_id).first()
    
    other_games = games.exclude(id=game_id)
    
    games_ordered = [game_selected] + list(other_games)
    
    formTournament = TournamentForm(request.POST or None, request.FILES or None, instance=tournament)
    if formTournament.is_valid() and request.POST:
        formTournament.save()
        tournament.avalaible_points = tournament.points
        tournament.save()  
        date_str = formTournament.cleaned_data.get('date')
        time_str = formTournament.cleaned_data.get('time')

        date_time = datetime.strptime(f'{date_str} {time_str}', '%Y-%m-%d %H:%M:%S')
        date_time_plus_5_hours = date_time + timedelta(hours=5)

        tournament_ref = db.collection('tournaments').document(tournament.uidRegister)
        
        current_data = tournament_ref.get().to_dict()
        
        data = {
            'creator': 'XxETDfQHDSB4lnLeDY0y',
            'name': tournament.name,
            'status': tournament.status,
            'game': tournament.game.UIDGame if tournament.game else None,
            'date': date_time_plus_5_hours,
            'inscribedPlayers': current_data.get('inscribedPlayers', []), 
            'players': tournament.players,
            'points': tournament.points,
            'avalaiblePoints': tournament.points,
            'rules': tournament.rules,
            'url': tournament.url,
            'imageURL': tournament.imageURL
        }
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
def reportView(request):
    firestore_users = get_all_users()
    return render(request,'players/report.html',{'firestore_users': firestore_users})

def generate_pdf(request):
    firestore_users = get_all_users()
    current_datetime = datetime.now().strftime("%Y%m%d-%H%M%S")

    template_path = 'players/report.html'
    template = get_template(template_path)
    html = template.render({'firestore_users': firestore_users})

    result = BytesIO()

    pisa_status = pisa.CreatePDF(html, dest=result)

    if pisa_status.err:
        return HttpResponse('Error al generar PDF: %s' % pisa_status.err)
    response = HttpResponse(result.getvalue(), content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="reporteUsuarios_{current_datetime}.pdf"'

    return response