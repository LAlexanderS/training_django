from django.shortcuts import render
from django.http.response import HttpResponse

def index(request):
	context: dict[str, str] = {
		'title': 'Home - Главная',
		'content': 'Магазин мебели HOME'
	}
	return render(request, 'main/index.html', context)

def about(request):
	context: dict[str, str] = {
		'title': 'Home - о нас',
		'content': 'о нас',
		'text_on_page': 'текст о магазине.'
	}
	return render(request, 'main/about.html', context)

