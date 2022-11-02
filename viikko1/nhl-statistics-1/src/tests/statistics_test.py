import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
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
        self.statistics = Statistics(PlayerReaderStub())

    def test_search(self):
        self.assertEqual(self.statistics.search("Semenko").team, "EDM")

    def test_team(self):
        print(self.statistics.team("EDM"))
        self.assertEqual(len(self.statistics.team("EDM")), 3)

    def test_search_empty(self):
        self.assertEqual(self.statistics.search("Jutila"), None)

    def test_top(self):
        self.assertEqual(self.statistics.top(1)[0].name, "Gretzky")