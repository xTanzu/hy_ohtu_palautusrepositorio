import requests
from player import Player

url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
response_json = requests.get(url).json()

players = []

for player_json in response_json:
    name = player_json['name']
    nationality = player_json['nationality']
    team = player_json['team']
    assists = player_json['assists']
    goals = player_json['goals']
    penalties = player_json['penalties']
    games = player_json['games']
    player = Player(name, nationality, team, assists, goals, penalties, games)
    players.append(player)

for player in sorted(players, key=lambda player: player.points(), reverse=True):
    if player.nationality == "FIN":
        print(repr(player))
