
class Cheese:
    def __init__(self):
        self.cheese_type = "cheddar"
    
    def get_cheese_type(self):
        return self.cheese_type
    
    def set_cheese_type(self, cheese_type):
        self.cheese_type = cheese_type

class Sauce:
    def __init__(self):
        self.sauce_type = "Prego"

    def get_sauce_type(self):
        return self.sauce_type

    def set_sauce_type(self, sauce_type):
        self.sauce_type = sauce_type
        print('Sauce type set to: ' + self.sauce_type)

class Toppings:
    def __init__(self):
        self.toppings_type = "Pepperoni"
        self.toppings_amount = 0

    def get_toppings_type(self):
        return self.toppings_type

    def get_toppings_amount(self):
        return self.toppings_amount

    def set_toppings_and_amount(self, toppings_type, toppings_amount):
        self.toppings_amount = toppings_amount
        self.toppings_type = toppings_type
        print('Toppings type set to: ' + self.toppings_type)
        print('Toppings amount set to: ' + str(self.toppings_amount))

class Dough:
    def __init__(self):
        self.is_wheat = False

    def get_dough_type(self):
        if self.is_wheat:
            return "wheat"
        else:
            return "regular"

    # Sets the dough type. is_wheat determines if it is wheat
    def set_dough_type(self, is_wheat):
        self.is_wheat = is_wheat

        print('Dough type set to: ' + self.get_dough_type())

