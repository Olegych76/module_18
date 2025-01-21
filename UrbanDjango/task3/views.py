from django.shortcuts import render

# Create your views here.


def platform(request):
    return render(request, 'third_task/platform.html')


def games(request):

    games_ = {
        'games': [
            {'name': 'Игра 1', 'url': '/cart'},
            {'name': 'Игра 2', 'url': '/cart'},
            {'name': 'Игра 3', 'url': '/cart'},
        ]
    }
    return render(request, 'third_task/games.html', games_)


def cart(request):
    return render(request, 'third_task/cart.html')
