import unittest
from src.pub import *
from src.drink import *

class TestPub(unittest.TestCase):
    def setUp(self):
        gin_drink = Drink("laser gin", 7, 35)
        drinks = [gin_drink]
        self.pub = Pub("Extravaganza", drinks)

    def test_has_name(self):
        self.assertEqual("Extravaganza", self.pub.name)
        
    def test_till_starts_0(self):
        self.assertEqual(0,self.pub.tills)

    def test_drink_count(self):
        # self.assertEqual(1, len(self.pub.drinks))
        self.assertEqual(1, self.pub.drink_count())


        

    
