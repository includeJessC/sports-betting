from datetime import datetime

import requests
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
    matches = []
    for game in data_list:
        if 'AA' in list(game.keys())[0]:
            date_start = datetime.fromtimestamp(int(game.get("AD", 0)))
            date_end = datetime.fromtimestamp(int(game.get("AO", 0)))
            team_1 = game.get("AE")
            team_2 = game.get("AF")
            id = game.get("~AA")
            parsing_ref = f'https://www.flashscorekz.com/match/{id}/#/match-summary'
            matches.append(
                {'id': id, 'name': f'{team_1} vs {team_2}', 'start_time': date_start, 'end_time': date_end, 'team1_name': team_1, 'team2_name': team_2,
                 'team1_res': game.get("AG"), 'team2_res': game.get("AH"), 'parsing_ref': parsing_ref, 'is_active': (date_start is not None)})
    return matches


def parse_competition(url):
    competition_id = url[(url.find('#')) + 2:(url.find('/table'))]
    response_result = requests.get(url=url, headers=headers)
    bp = BeautifulSoup(response_result.text, 'lxml')
    title = bp.find(attrs={'property': 'og:title'})
    name = title.get('content')
    url = url[:(url.find('#'))]
    url_not_finished_matches = url + 'fixtures/'
    url_finished_matches = url + 'results/'
    response_not_finished = requests.get(url=url_not_finished_matches, headers=headers)
    response_finished = requests.get(url=url_finished_matches, headers=headers)
    finished_matches = manager(response_finished)
    not_finished_matches = manager(response_not_finished)
    return {'competition_id': competition_id, "name": name, 'is_active': True if len(not_finished_matches) else False,
           'parsing_ref': url, 'ended_matches': finished_matches, 'not_ended_matches': not_finished_matches}


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
    second_team = del_blanks(res[(res.find(' - ')) + 3:-3])
    print(first_team, second_team, score)
