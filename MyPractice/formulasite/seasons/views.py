from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *

# Create your views here.
menu = [{'title': 'Личный зачет', 'url_name': 'drivers_standings'},
        {'title': 'Командный зачет', 'url_name': 'constructors_standings'},
        {'title': 'Новости', 'url_name': 'news'},
        {'title': 'Авторизация', 'url_name': 'login'},
        ]
seasons_numbers = []
for i in range(1995, 2024):
    seasons_numbers.append(i)


def index(request):
    posts = Season.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',
    }
    return render(request, 'seasons/index.html', context=context)


def seasons(request):
    posts = Season.objects.all()
    context = {
        'posts': posts,
        'title': 'Все сезоны Ф1',
    }

    return render(request, 'seasons/seasons.html', context=context)


def call_seasons_number(request, season_number):
    return HttpResponse(f'Отображение сезона с id = {season_number}')


def teams(request):
    return HttpResponse(f'Выберите команду')


def call_team_name(request, team_name):
    return HttpResponse(f'Команда {team_name}')


def drivers(request):
    return HttpResponse(f'Выберите гонщика')


def call_drivers_name(request, driver_name):
    if type(driver_name) != str:
        raise Http404
    return HttpResponse(f'Гонщик {driver_name}')


def tracks(request):
    return HttpResponse('Выберите трек')


def stories(request):
    return HttpResponse('Выберите историю')


def news(request):
    return HttpResponse('Почитаем новости')


def drivers_standings(request):
    return HttpResponse('зачет пилотов')


def constructors_standings(request):
    return HttpResponse('зачет команд')


def login(request):
    return HttpResponse('Регистрация')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')