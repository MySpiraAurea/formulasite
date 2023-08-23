from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('seasons/', seasons, name='seasons'),
    path('seasons/<int:season_number>/', call_seasons_number, name='post'),
    path('teams/', teams, name='teams'),
    path('teams/<str:team_name>/', call_team_name, name='team_name'),
    path('drivers/', drivers, name='drivers'),
    path('drivers/<str:driver_name>/', call_drivers_name, name='driver_name'),
    path('tracks/', tracks, name='tracks'),
    path('stories/', stories, name='stories'),
    path('news/', news, name='news'),
    path('drivers_standings/', drivers_standings, name='drivers_standings'),
    path('constructors_standings/', constructors_standings, name='constructors_standings'),
    path('login/', login, name='login'),
]