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
        self._reader = PlayerReaderStub()
        self.players = self._reader.get_players()
        self.stats = Statistics(PlayerReaderStub())

    def test_player_is_found_correctly(self):
        self.assertEqual(str(self.stats.search("Semenko")),
                                "Semenko EDM 4 + 12 = 16")

    def test_player_not_found_returns_none(self):
        self.assertEqual(self.stats.search("Non-existent"), None)

    def test_nonexistent_team_returns_empty_list(self):
        self.assertEqual(self.stats.team("Non-existent"), [])

    def test_top_score_is_correct(self):
        self.assertEqual(str(self.stats.top_scorers(1)[0]),
                                "Gretzky EDM 35 + 89 = 124")