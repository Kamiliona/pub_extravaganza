import unittest
from src.customer import *
from src.drink import *
from src.pub import *

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Violet",72,10000)
    
    def test_has_name(self):
        self.assertEqual("Violet", self.customer.name)
    
    def test_has_wallet(self):
        self.assertEqual(10000, self.customer.wallet)

    def test_buys_drink__sufficient_funds(self):
        gin_drink = Drink("laser gin", 7,35)
        drinks = [gin_drink]
        pub  = Pub("Extravaganza", drinks)
        self.customer.buys_drink("laser gin", pub)
        self.assertEqual(9993, self.customer.wallet)
        self.assertEqual(7, pub.tills)
        self.assertEqual(35, self.customer.level_of_drunkness)

    def test_buys_drink__insufficient_funds(self):
        gin_drink = Drink("laser gin", 7,35)
        drinks = [gin_drink]
        pub  = Pub("Extravaganza", drinks)
        customer = Customer("Ian",22, 1)
        customer.buys_drink("laser gin", pub)
        self.assertEqual(1, customer.wallet)
        self.assertEqual(0, pub.tills)
        self.assertEqual(0, customer.level_of_drunkness)

    def test_buys_drink__underage(self):
        gin_drink = Drink("laser gin", 7,35)
        drinks = [gin_drink]
        pub  = Pub("Extravaganza", drinks)
        customer = Customer("Zsolt",16, 100)
        customer.buys_drink("laser gin", pub)
        self.assertEqual(100, customer.wallet)
        self.assertEqual(0, pub.tills)
        self.assertEqual(0, customer.level_of_drunkness)


        # def test_buys_drink__insufficient_funds(self):
        # gin_drink = Drink("laser gin", 7)
        # drinks = [gin_drink]
        # pub  = Pub("Extravaganza", drinks)
        # customer = Customer("Ian",22, 1)
        # customer.buys_drink("laser gin", pub)
        # self.assertEqual(1, customer.wallet)
        # self.assertEqual(0, pub.tills)

        