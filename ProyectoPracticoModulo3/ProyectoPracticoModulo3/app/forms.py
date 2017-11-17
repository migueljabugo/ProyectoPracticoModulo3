"""
Definition of forms.
"""

from django import forms
from app.models import Game

class form_game(forms.ModelForm):
	class Meta:
		model = Game
		fields = ("name", 
			'publisher', 
			'year', 
			'genre', 
			'platform', 
			'score', 
			'online', 
			'pegi'
			)


class form_search(forms.Form):
	busqueda = forms.CharField(label='Shearch', max_length=100)