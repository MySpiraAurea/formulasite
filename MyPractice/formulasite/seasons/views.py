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

sidebar = [{'title': 'Сезоны', 'function': 'seasons'},
           {'title': 'Гонщики', 'function': 'drivers'},
           {'title': 'Команды', 'function': 'teams'},
           {'title': 'Трассы', 'function': 'tracks'},
           {'title': 'Истории', 'function': 'stories'},
           ]

seasons_numbers = []
for i in range(1995, 2024):
    seasons_numbers.append(i)


def index(request):
    posts = News.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',
        'category': 'news',
        'sidebar': sidebar,
    }
    return render(request, 'seasons/index.html', context=context)


def seasons(request):
    posts = Season.objects.all()
    context = {
        'posts': posts,
        'title': 'Все сезоны Ф1',
        'category': 'seasons',
        'sidebar': sidebar,
    }

    return render(request, 'seasons/seasons.html', context=context)


def call_season_number(request, season_number):
    return HttpResponse(f'Отображение сезона с id = {season_number}')


def teams(request):
    teams = Team.objects.all()
    context = {
        'teams': teams,
        'title': 'Все команды',
        'category': 'teams',
        'sidebar': sidebar,
    }

    return render(request, 'seasons/teams.html', context=context)

    return HttpResponse(f'Выберите команду')


def call_team_name(request, team_name):
    return HttpResponse(f'Команда {team_name}')


def drivers(request):
    drivers = Driver.objects.all()
    context = {
        'drivers': drivers,
        'title': 'Все пилоты',
        'category': 'drivers',
        'sidebar': sidebar,
    }

    return render(request, 'seasons/drivers.html', context=context)


def call_driver_name(request, driver_name):
    if type(driver_name) != str:
        raise Http404
    return HttpResponse(f'Гонщик {driver_name}')


def tracks(request):
    tracks = Track.objects.all()
    context = {
        'tracks': tracks,
        'title': 'Все трассы',
        'category': 'tracks',
        'sidebar': sidebar,
    }

    return render(request, 'seasons/tracks.html', context=context)


def show_track(request, track_name):
    return HttpResponse(f'Трасса {track_name}')


def stories(request):
    stories = Story.objects.all()
    context = {
        'stories': stories,
        'title': 'Истории',
        'category': 'stories',
        'sidebar': sidebar,
    }

    return render(request, 'seasons/stories.html', context=context)


def show_story(request, story_number):
    return HttpResponse(f'История о {story_number}')


def news(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Новости',
    }

    return render(request, 'seasons/news.html', context=context)


def show_news(request, news_number):
    return HttpResponse(f'отображение статьи {news_number}')


def drivers_standings(request):
    return HttpResponse('зачет пилотов')


def constructors_standings(request):
    return HttpResponse('зачет команд')


def login(request):
    return HttpResponse('Регистрация')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')