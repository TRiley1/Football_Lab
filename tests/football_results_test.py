import unittest
from src.football_results import *

class FootballResultsTest(unittest.TestCase):
    pass
    # Test we get the right result string for a final score dictionary representing -

        # Home win
        # Away win
        # Draw

    # Test we get right list of result strings for a list of final score dictionaries. 

    def test_home_win(self):
        result = {
        "home_score" : 2,
        "away_score" : 0
        }
        self.assertEqual("Home Win", get_result(result))

    def test_away_win(self):
        result = {
        "home_score" : 0,
        "away_score" : 1
        }
        self.assertEqual("Away win", get_result(result))

if __name__ == "__main__":
    unittest.main()
