import requests
from player import Player


class PlayerReader:

    def __init__(self, url:str):
        self.url = url

    def get_players(self):
        response = requests.get(self.url).json()
        players = []

        for player_info in response:
            name = player_info['name']
            nationality = player_info['nationality']
            team = player_info['team']
            assists = player_info['assists']
            goals = player_info['goals']
            penalties = player_info['penalties']
            games = player_info['games']
            player = Player(name, nationality, team, assists, goals, penalties, games)
            players.append(player)

        return players


class PlayerStats:
    
    def __init__(self, reader:PlayerReader):
        self.reader = reader
        self.players = self.reader.get_players()

    def top_scorers_by_nationality(self, nationality:str):
        players_by_nationality = filter(lambda player: player.nationality == nationality, self.players)
        return sorted(players_by_nationality, key=lambda player: player.points(), reverse=True)


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(repr(player))

if __name__ == "__main__":
    main()
