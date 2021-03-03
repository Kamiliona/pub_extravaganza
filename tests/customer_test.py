import unittest
from src.customer import *
from src.drink import *
from src.pub import *

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Violet",10000)
    
    def test_has_name(self):
        self.assertEqual("Violet", self.customer.name)
    
    def test_has_wallet(self):
        self.assertEqual(10000, self.customer.wallet)

    def test_buys_drink(self):
        gin_drink = Drink("laser gin", 7)
        drinks = [gin_drink]
        pub  = Pub("Extravaganza", drinks)
        self.customer.buys_drink("laser gin", pub)
        self.assertEqual(9993, self.customer.wallet)
        self.assertEqual(7, pub.tills)
