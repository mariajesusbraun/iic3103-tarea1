from django.contrib import admin
from django.urls import include, path
from polls.views import get_seasons, get_episodes_bb, get_episodes_bcs, get_episode, get_character, get_search

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', get_seasons, name='Seasons View'),
    path('episodesBB/<season>', get_episodes_bb, name='Episodes View'),
    path('episodesBCS/<season>', get_episodes_bcs, name='Episodes View'),
    path('episode/<title>', get_episode, name='Episode View'),
    path('character/<name>', get_character, name='Character View'),
    path('search', get_search, name='Search View'),
]
