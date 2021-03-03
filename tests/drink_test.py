import unittest
from src.drink import *

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("laser gin",7)

    def test_drink_has_name(self):
        self.assertEqual("laser gin", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(7, self.drink.price)

    