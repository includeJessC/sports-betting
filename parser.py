import json
import requests
from datetime import datetime


headers = {"x-fsign": "SW9D1eZo"}


def main():
    url = f'https://www.flashscorekz.com/football/england/premier-league/#/nunhS7Vn/table/overall'
    url1 = f'https://www.flashscorekz.com/football/england/premier-league/fixtures/' # url незавершенных матчей
    url2 = f'https://www.flashscorekz.com/football/england/premier-league/results/' # url завершенных матчей
    response = requests.get(url=url2, headers=headers)
    data = response.text.split('¬')
    data_list = [{}]
    for item in data:
        key = item.split('÷')[0]
        value = item.split('÷')[-1]

        if '~' in key:
            data_list.append({key: value})
        else:
            data_list[-1].update({key: value})
    print(data_list)
    for game in data_list:
        if 'AA' in list(game.keys())[0]:
            date_start = datetime.fromtimestamp(int(game.get("AD", 0)))
            date_end = datetime.fromtimestamp(int(game.get("ADE", 0)))
            team_1 = game.get("AE")
            team_2 = game.get("AF")
            score = f'{game.get("AG")} : {game.get("AH")}'
            print(date_start, date_end, team_1, team_2, score)



if __name__ == '__main__':
    main()