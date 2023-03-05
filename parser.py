import json
import requests
from datetime import datetime
from bs4 import BeautifulSoup

headers = {"x-fsign": "SW9D1eZo"}
def manager(response):
    data = response.text.split('¬')
    data_list = [{}]
    for item in data:
        key = item.split('÷')[0]
        value = item.split('÷')[-1]
        if '~' in key:
            data_list.append({key: value})
        else:
            data_list[-1].update({key: value})
    for game in data_list:
        if 'AA' in list(game.keys())[0]:
            date_start = datetime.fromtimestamp(int(game.get("AD", 0)))
            date_end = datetime.fromtimestamp(int(game.get("AO", 0)))
            team_1 = game.get("AE")
            team_2 = game.get("AF")
            id = game.get("~AA")
            parsing_ref = f'https://www.flashscorekz.com/match/{id}/#/match-summary'
            score = f'{game.get("AG")} : {game.get("AH")}'
            print(id, date_start, date_end, team_1, team_2, score, parsing_ref)

def parse_competition(url):
    url = url[:(url.find('#'))]
    url_not_finished_matches = url + 'fixtures/'
    url_finished_matches = url + 'results/'
    response_not_finished = requests.get(url=url_not_finished_matches, headers=headers)
    response_finished = requests.get(url=url_finished_matches, headers=headers)
    manager(response_finished)
    manager(response_not_finished)

def del_blanks(string):
    i = 0
    while string[i] == ' ':
        string = string[1:]
    while string[-1] == ' ':
        string = string[:-1]
    return string

def parse_match(url):
    response_match = requests.get(url=url, headers=headers)
    print(response_match.text)
    bp = BeautifulSoup(response_match.text, 'lxml')
    print(bp)
    title = bp.find(attrs={'name': 'og:title'})
    res = title.get('content')
    score = ''
    if res[-1].isnumeric() and res[-3].isnumeric():
        score = f'{res[-3]} : {res[-1]}'
    first_team = del_blanks(res[:(res.find(' - '))])
    second_team = del_blanks(res[(res.find(' - '))+3:-3])
    print(first_team, second_team, score)
