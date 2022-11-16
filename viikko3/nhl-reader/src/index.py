import requests
from player import Player

url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
response_json = requests.get(url).json()

players = []

for player_json in response_json:
    name = player_json['name']
    nationality = player_json['nationality']
    team = player_json['team']
    stats = {}
    stats['assists'] = player_json['assists']
    stats['goals'] = player_json['goals']
    stats['penalties'] = player_json['penalties']
    stats['games'] = player_json['games']
    player = Player(name, nationality, team, stats)
    players.append(player)

for player in sorted(players):
    if player.nationality == "FIN":
        print(repr(player))

