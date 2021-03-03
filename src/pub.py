class Pub:
    def __init__(self, name, drinks):
        self.name = name 
        self.drinks = drinks
        self.tills = 0

    def drink_count(self):
        return len(self.drinks)

    def find_drink_by_name(self, name):
        for drink in self.drinks:
            if drink.name == name:
                return drink
        # return None
