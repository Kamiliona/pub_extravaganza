class Customer:
    def __init__ (self, name, wallet=0):
        self.name = name
        self.wallet = wallet

    def buys_drink(self, drink_name, pub):
        drink = pub.find_drink_by_name(drink_name)
        if self.wallet >= drink.price:
            self.wallet -= drink.price
            pub.tills += drink.price

