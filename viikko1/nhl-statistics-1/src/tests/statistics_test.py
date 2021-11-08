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
        self.players = PlayerReaderStub.get_players()
        self.stats = Statistics(PlayerReaderStub())

    def test_player_is_found_correctly(self):
        self.assertAlmostEqual(self.stats.search("Semenko"),
                                Player("Semenko", "EDM", 4, 12))