from django.db import models
from .choices import estado
# Create your models here.

class Game(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name= 'Nombre')
    company = models.CharField(max_length=100, verbose_name= 'Empresa')
    details = models.CharField(max_length=500, verbose_name= 'Detalles')
    status = models.BooleanField(verbose_name= 'Activo')
    image = models.ImageField(upload_to='tournaments/images/games/', verbose_name= 'Imagen', null=True)
    def __str__(self):
        fila = 'Nombre: '+ self.name  + ' - ' + 'Empresa: ' + self.company
        return fila

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()

    class Meta:
        verbose_name = 'game'
        verbose_name_plural = 'games'
        db_table = 'games'

class Tournament(models.Model):
    id = models.AutoField(primary_key=True)
    game = models.ForeignKey(Game, null=True, blank=True, on_delete=models.CASCADE, verbose_name= 'Juego')
    name = models.CharField(max_length=100, verbose_name= 'Titulo')
    status = models.CharField(max_length=1, choices=estado, default='C', verbose_name= 'Estado')
    date = models.DateField( verbose_name= 'Fecha')
    time = models.TimeField( verbose_name= 'Hora')
    max_participants = models.IntegerField( verbose_name= 'Participantes')
    points = models.IntegerField( verbose_name= 'Puntaje')
    rules = models.TextField(max_length=3000, verbose_name= 'Reglamento')
    url = models.CharField(max_length=1000,  verbose_name= 'Link')
    image = models.ImageField(upload_to='tournaments/images/', verbose_name= 'Imagen', null=True)

    def __str__(self):
        fecha = self.date.strftime('%d-%m-%Y')
        hora = self.time.strftime('%I:%M %p')
        fila = 'Titulo: ' + self.name + ' - ' + 'Fecha: ' + fecha + ' ' + 'Hora: ' + hora
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()
    class Meta:
        verbose_name = 'tournament'
        verbose_name_plural = 'tournaments'
        db_table = 'tournaments'

class Player(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, verbose_name= 'Nombre')
    email = models.EmailField(max_length=100, verbose_name= 'Email')
    phone = models.CharField(max_length=20, verbose_name= 'Telefono')
    image = models.ImageField(upload_to='tournaments/images/players/profile/', verbose_name= 'Imagen', null=True)
    points = models.IntegerField(verbose_name= 'Puntaje')    


    def __str__(self):
        fila = 'Nombre: ' + self.username + ' - ' + 'Puntaje: ' + str(self.points)
        return fila

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()
    class Meta:
        verbose_name = 'player'
        verbose_name_plural = 'players'
        db_table = 'players'