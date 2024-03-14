from django import forms
from .models import Tournament, Player
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = '__all__'

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'

class AdminForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
