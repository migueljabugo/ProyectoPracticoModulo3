"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from app.models import Game
from app.forms import form_game
from app.forms import form_search

def home(request):
	assert isinstance(request, HttpRequest)
	games = Game.objects.all().order_by("name")
	return render(
		request,
		'app/index.html',
		{
			'title':'Videogames Codex',
			'games':games
		}
	)

def notFound(request):
	assert isinstance(request, HttpRequest)
	return render(
		request,
		'app/404.html',
		{
            'title':'Pagina no encontrada',
        }
	)

def show_game(request, id):
	assert isinstance(request, HttpRequest)
	game = Game.objects.get(pk=id)
	return render(
		request,
		'app/show.html',
		{
			'title':'Show Game',
			'game':game
		}
	)


def new_game(request):
	assert isinstance(request, HttpRequest)
	if (request.method == 'POST'):
		formulario = form_game(request.POST)
		if (formulario.is_valid()):
			game = formulario.save()
			return HttpResponseRedirect('/game/' + str(game.id))

	elif (request.method == 'GET'):
		return render(
			request,
			'app/form_game.html',
			{
				'title':'New game',
				'action':'/new',
				'form': form_game(),
			}
		)
	else:
		return render(request, 'app/404.html')



def edit_game(request, id):
	assert isinstance(request, HttpRequest)
	game = Game.objects.get(pk=id)
	if (request.method == 'POST'):
		formulario = form_game(request.POST, instance=game)
		if (formulario.is_valid()):
			game = formulario.save()
			return HttpResponseRedirect('/game/' + str(game.id))
	elif (request.method == 'GET'):
		return render(
			request,
			'app/form_game.html',
			{
				'title':'Edit game',
				'action':'/edit/' + str(game.id),
				'form': form_game(instance = game),
				"game":game
			}
		)
	else:
		return render(request, 'app/404.html')

def remove_game(request, id):
	assert isinstance(request, HttpRequest)
	game = Game.objects.get(pk=id)
	game.delete()
	return HttpResponseRedirect('/')

def ranking(request):
	assert isinstance(request, HttpRequest)
	games = Game.objects.values_list("name", "score", "id").order_by("score").reverse()
	return render(
		request,
		'app/ranking.html',
		{
			'title':'Ranking',
			"games":games
		}
	)

def search(request):
	assert isinstance(request, HttpRequest)
	if (request.method == 'POST'):
		result_form = form_search(request.POST)
		busqueda = result_form['busqueda'].data
		games = Game.objects.filter(name__icontains=busqueda)
		if(len(games)>0):
			return HttpResponseRedirect('/game/'+str(games[0].id))
		else:
			return HttpResponseRedirect('/')



	elif (request.method == 'GET'):
		return render(
			request,
			'app/form_search.html',
			{
				'title':'Search Game',
				'form': form_search(),
			}
		)
	else:
		return render(request, 'app/404.html')
