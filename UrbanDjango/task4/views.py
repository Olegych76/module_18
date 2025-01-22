from django.shortcuts import render

# Create your views here.


def platform(request):
    return render(request, 'fourth_task/platform.html')


def games(request):
    games_ = {'games': ['Игра 1', 'Игра 2', 'Игра 3',]}
    return render(request, 'fourth_task/games.html', games_)


def cart(request):
    return render(request, 'fourth_task/cart.html')
