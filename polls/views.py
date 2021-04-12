from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
import requests
import json

def get_seasons(request):
    url_bb = "https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad"
    r_bb = requests.get(url_bb, headers={'Authorization':'Bearer %s' % 'access_token'})
    episodes_bb = r_bb.json()
    seasons_bb_list = []
    for i in range(len(episodes_bb)):
        seasons_bb_list.append(episodes_bb[i]['season'])
    seasons_bb = sorted(list(set(seasons_bb_list)))
    url_bcs = "https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul"
    r_bcs = requests.get(url_bcs, headers={'Authorization':'Bearer %s' % 'access_token'})
    episodes_bcs = r_bcs.json()
    seasons_bcs_list = []
    for i in range(len(episodes_bcs)):
        seasons_bcs_list.append(episodes_bcs[i]['season'])
    seasons_bcs = sorted(list(set(seasons_bcs_list)))
    context = {
        'seasons_bb' : seasons_bb,
        'seasons_bcs' : seasons_bcs,
    }
    return render(request, 'seasons.html', context)

def get_episodes_bb(request, season):
    url = "https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad"
    r = requests.get(url, headers={'Authorization':'Bearer %s' % 'access_token'})
    episodes = r.json()
    episodes_names_list = []
    for i in range(len(episodes)):
        if episodes[i]['season'] == season:
            episodes_names_list.append(episodes[i]['title'])
    context = {
        'episodes' : episodes_names_list,
    }
    return render(request, 'episodes.html', context)

def get_episodes_bcs(request, season):
    url = "https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul"
    r = requests.get(url, headers={'Authorization':'Bearer %s' % 'access_token'})
    episodes = r.json()
    episodes_names_list = []
    for i in range(len(episodes)):
        if episodes[i]['season'] == season:
            episodes_names_list.append(episodes[i]['title'])
    context = {
        'episodes' : episodes_names_list,
    }
    return render(request, 'episodes.html', context)

def get_episode(request, title):
    url = "https://tarea-1-breaking-bad.herokuapp.com/api/episodes"
    r = requests.get(url, headers={'Authorization':'Bearer %s' % 'access_token'})
    episodes = r.json()
    context = ''
    for i in range(len(episodes)):
        if episodes[i]['title'].lower() == title.lower():
            context = {
                'episode' : episodes[i]
            }
    if context == '':
        title2 = title.lower().split()
        for i in range(len(episodes)):
            episode = episodes[i]['title'].lower().split()
            k = 0
            if len(title2) < len(episode):
                for j in range (len(title2)):
                    if title2[j] == episode[j]:
                        k += 1
            if k == len(title2):
                context = {
                    'episode' : episodes[i]
                }
    return render(request, 'episode.html', context)

def get_character(request, name):
    name_list = name.split()
    name = '+'.join(name_list)
    url_c = "https://tarea-1-breaking-bad.herokuapp.com/api/characters?name=" + name
    r_c = requests.get(url_c, headers={'Authorization':'Bearer %s' % 'access_token'})
    char_info = r_c.json() 
    url_q = "https://tarea-1-breaking-bad.herokuapp.com/api/quote?author=" + name
    r_q = requests.get(url_q, headers={'Authorization':'Bearer %s' % 'access_token'})
    quotes = r_q.json()
    context = {
        'characters' : char_info,
        'quotes' : quotes,
    }
    return render(request, 'character.html', context)

def get_search(request):
    name = request.GET['search']
    actual_list = ['']
    characters_list = []
    i = 0
    while actual_list != []:
        url = "https://tarea-1-breaking-bad.herokuapp.com/api/characters?name=" + name + "&offset=" + str(i)
        search_characters = requests.get(url, headers={'Authorization':'Bearer %s' % 'access_token'})
        characters = search_characters.json()
        actual_list = characters
        for character in characters:
            characters_list.append(character)
        i += 10
    context = {
        'characters' : characters_list,
    }
    return render(request, 'search.html', context)