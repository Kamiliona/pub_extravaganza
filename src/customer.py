class Customer:
    def __init__ (self, name, age, wallet=0):
        self.name = name
        self.age = age
        self.wallet = wallet
        self.level_of_drunkness = 0

    def buys_drink(self, drink_name, pub):
        drink = pub.find_drink_by_name(drink_name)
        if self.wallet >= drink.price and self.age >= 18:
            self.wallet -= drink.price
            pub.tills += drink.price
            self.level_of_drunkness += drink.alcohol_level

#  def buys_drink(self, drink_name, pub):
#         drink = pub.find_drink_by_name(drink_name)
#         if self.wallet >= drink.price:
#             self.wallet -= drink.price
#             pub.tills += drink.price
