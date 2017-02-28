from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	return render(request, 'ninja_app/index.html')

def ninjas(request):
	context = {
		'check': False,
	}
	return render(request, 'ninja_app/ninja.html', context)

def color(request, color):

	context = {
		'color': color,
		'check': True
	}
	return render(request, 'ninja_app/ninja.html', context)
