from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('seasons/', seasons, name='seasons'),
    path('seasons/<int:season_number>/', call_season_number, name='season_number'),
    path('teams/', teams, name='teams'),
    path('teams/<str:team_name>/', call_team_name, name='team_name'),
    path('drivers/', drivers, name='drivers'),
    path('drivers/<str:driver_name>/', call_driver_name, name='driver_name'),
    path('tracks/', tracks, name='tracks'),
    path('tracks/<str:track_name>/', show_track, name='show_track'),
    path('stories/', stories, name='stories'),
    path('stories/<str:story_number>/', show_story, name='show_story'),
    path('news/', news, name='news'),
    path('news/<str:news_number>/', show_news, name='show_news'),
    path('drivers_standings/', drivers_standings, name='drivers_standings'),
    path('constructors_standings/', constructors_standings, name='constructors_standings'),
    path('login/', login, name='login'),
]