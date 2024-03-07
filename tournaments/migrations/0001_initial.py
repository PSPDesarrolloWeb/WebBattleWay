# Generated by Django 5.0.2 on 2024-02-18 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('game', models.CharField(max_length=100, verbose_name='Juego')),
                ('name', models.CharField(max_length=100, verbose_name='Titulo')),
                ('status', models.CharField(max_length=10, verbose_name='Estado')),
                ('date', models.DateField(verbose_name='Fecha')),
                ('time', models.TimeField(verbose_name='Hora')),
                ('max_participants', models.IntegerField(verbose_name='Participantes')),
                ('points', models.IntegerField(verbose_name='Puntaje')),
                ('rules', models.CharField(max_length=3000, verbose_name='Reglamento')),
                ('url', models.CharField(max_length=1000, verbose_name='Link')),
                ('image', models.ImageField(null=True, upload_to='tournaments/images/', verbose_name='Imagen')),
            ],
        ),
    ]