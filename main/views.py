from django.shortcuts import render
from django.http.response import HttpResponse

def index(request):
	context: dict[str, str] = {
		'title': 'home',
		'content': 'main page of this page',
		'list': ['first', 'second'],
		'dict': {'first': 1},
		'is_auth': False

	}
	return render(request, 'main/index.html', context)

def about(request):
	return HttpResponse('about page')

