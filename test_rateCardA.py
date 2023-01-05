import unittest
from main import rateCardA


class TestRateCardA(unittest.TestCase):
    def test_rate_card_a(self):
        # Test the default case where length is 1
        rate_card = rateCardA()
        self.assertEqual(rate_card["Cabinet"], 1000)
        self.assertEqual(rate_card["verge"], 50)
        self.assertEqual(rate_card["road"], 100)
        self.assertEqual(rate_card["Chamber"], 200)
        self.assertEqual(rate_card["Pot"], 100)

        # Test the case where length is 2
        rate_card = rateCardA(length=2)
        self.assertEqual(rate_card["Cabinet"], 1000)
        self.assertEqual(rate_card["verge"], 100)
        self.assertEqual(rate_card["road"], 200)
        self.assertEqual(rate_card["Chamber"], 200)
        self.assertEqual(rate_card["Pot"], 100)
