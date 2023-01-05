import unittest
from main import rateCardB


class TestRateCardB(unittest.TestCase):
    def test_rateCardB(self):
        # Test default values for length and lengthOfTrench
        result = rateCardB()
        expected = {
            "Cabinet": 1200,
            "verge": 40,
            "road": 80,
            "Chamber": 200,
            "Pot": 20,
        }
        self.assertEqual(result, expected)

        # Test different values for length and lengthOfTrench
        result = rateCardB(length=2, lengthOfTrench=3)
        expected = {
            "Cabinet": 1200,
            "verge": 80,
            "road": 160,
            "Chamber": 200,
            "Pot": 60,
        }
        self.assertEqual(result, expected)

