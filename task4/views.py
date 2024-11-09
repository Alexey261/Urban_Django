from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    return render(request, 'fourth_task/platform.html')

def cart(request):
    return render(request, 'fourth_task/cart.html')

def games(request):
    gds = ['Counter-Strike', 'Quake III Arena', 'Doom 2: Hell on Earth']
    data = {'goods': gds}
    return render(request, 'fourth_task/games.html', context=data)



