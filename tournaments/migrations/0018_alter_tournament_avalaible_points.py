# Generated by Django 5.0.2 on 2024-07-07 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0017_tournament_avalaible_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='avalaible_points',
            field=models.IntegerField(verbose_name='Puntaje disponible'),
        ),
    ]