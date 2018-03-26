
'''
A pizza that can be baked, and ordered
TODO : Complete the pizza class using the subclasses below.
'''
class Pizza:

    def __init__(self):
        self.baked = False

    def bake_pizza(self):
        print('not implemented')

    def order_pizza(self):
        # TODO : This class should print out all the details of a baked pizza
        # if the pizza isn't baked, this function should give me an error
        print('not implemented')

'''
Cheese that can be set
'''
class Cheese:
    '''
    @rachel, look at the changes I made here.
    This allows us to set our cheese type when creating our cheese object.
    E.g.
        c = Cheese("muenster")
    The "cheese_type = None" part means that if a cheese type is not provided, the
    object will revert to defaults. the = None is called a default
    "if cheese_type:" means simply that if the cheese type is not None, do the 
    following
    '''
    def __init__(self, cheese_type = None):
        self.cheese_type = "cheddar"
        if cheese_type:
            self.cheese_type = cheese_type
    
    def get_cheese_type(self):
        return self.cheese_type
    
    def set_cheese_type(self, cheese_type):
        self.cheese_type = cheese_type

# TODO : Add defaults like the Cheese class
class Sauce:
    def __init__(self):
        self.sauce_type = "Prego"

    def get_sauce_type(self):
        return self.sauce_type

    def set_sauce_type(self, sauce_type):
        self.sauce_type = sauce_type
        print('Sauce type set to: ' + self.sauce_type)

# TODO : Add defaults like the Cheese class
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

# TODO : Add defaults like the Cheese class
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

