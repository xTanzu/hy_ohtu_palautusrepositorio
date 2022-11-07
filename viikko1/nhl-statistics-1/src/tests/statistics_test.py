import unittest
# from player_reader_stub import PlayerReaderStub
from player import Player
from statistics import Statistics


class PlayerReaderStub():

    def __init__(self):
        self._url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players.txt"

    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.reader = PlayerReaderStub()
        self.statistics = Statistics(self.reader)

    def test_search_when_found(self):
        player = self.statistics.search("Semenko")
        self.assertEqual(player.name, "Semenko")

    def test_search_when_not_found(self):
        player = self.statistics.search("imaginary_player")
        self.assertEqual(player, None)

    def test_team(self):
        team_players = self.statistics.team("EDM")
        self.assertEqual(len(team_players), 3)
        team_players[0] == "Semenko"
        team_players[1] == "Kurri"
        team_players[2] == "Gretzky"

    def test_top(self):
        correct_top_player_names = ["Gretzky", "Lemieux", "Yzerman", "Kurri", "Semenko"]
        top_players = self.statistics.top(4)
        for i in range(5):
            self.assertEqual(top_players[i].name, correct_top_player_names[i])

