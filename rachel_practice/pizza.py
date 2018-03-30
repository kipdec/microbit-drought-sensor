
'''
A pizza that can be baked, and ordered
TODO : Complete the pizza class using the subclasses below.
'''

# For the Pizza class I though I should put all of the pieces as subclasses into Pizza.
# Unfortunately my spacing is wrong almost everywhere and I could only get down to line 34 to
# the point where I cannot find the spacing error. So I cannot even see if this would have worked
# My other thought is this won't work because we have multiple sets of the "__init__", "get....type"
# and "set....type" which maybe there should be "__init__" and each sublcass is defined and then go
# on to the next pieces (get...type). I feel like there is a more efficent way to put these
# things together.


class Pizza:

    def __init__(self, sauce=None, toppings=None, dough=None, cheese=None):
        # Price for pizza without toppings
        self.base_rate = 10
        self.sauce = Sauce(sauce)
        self.toppings = Toppings(toppings)
        self.dough = Dough(dough)
        self.cheese = Cheese(cheese)
        self.is_baked = False
        self.cost = 0

    def get_sauce_type(self):
        return self.sauce.get_sauce_type()

    def set_sauce_type(self, sauce_type):
        self.sauce.set_sauce_type(sauce_type)

    def get_cheese_type(self):
        return self.cheese.get_cheese_type()

    def set_cheese_type(self, cheese_type):
            self.cheese.set_cheese_type(cheese_type)

    def get_toppings_type(self):
        return self.toppings.get_toppings_type()

    def get_toppings_amount(self):
        return self.toppings.get_toppings_amount()

    def set_toppings_and_amount(self, toppings_type, toppings_amount):
        self.toppings.set_toppings_and_amount(
            toppings_type, toppings_amount)

    def calculate_toppings(self):
        # This function calculates the cost of the pizza and the toppings
        # Each topping costs $.50
        # The toppings are then added to the base rate and stored in self.cost
        self.cost = (self.base_rate + (self.get_toppings_amount() * .5))

    def get_dough_type(self):
        return self.dough.get_dough_type()

    def set_dough_type(self, is_wheat):
        self.dough.set_dough_type(is_wheat)

    def bake_pizza(self):
        self.is_baked = True

    def get_bake_type(self):
        if self.is_baked:
            return "baked"
        return "not yet baked"

    def order_pizza(self, customer_name):
        # TODO : This class should print out all the details of a baked pizza
        # if the pizza isn't baked, this function should give me an error
        if self.is_baked:
            self.calculate_toppings()
            spacer = "================================"
            print(customer_name + "'s pizza:")
            print(spacer)
            print("Sauce: " + self.get_sauce_type())
            print("Cheese: " + self.get_cheese_type())
            print("Dough: " + self.get_dough_type())
            print("Toppings Type: " + self.get_toppings_type())
            print("Toppings Amount: " + str(self.get_toppings_amount()))
            print(spacer)
            print("Total cost: " + str(self.cost))
        else:
            print("pizza not yet baked")

# the spacing was all messed up here but I got it!!


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
# This is SICK. So is it allowing me to switch it so easily because we did cheese_type = None? or the if statment?
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
# And this is saying, if I don't specify the type of sauce, there is none.
class Sauce:
    def __init__(self, sauce_type = None):
        self.sauce_type = "redSauce"
        if sauce_type:
            self.sauce_type = sauce_type

    def get_sauce_type(self):
        return self.sauce_type

    def set_sauce_type(self, sauce_type):
        self.sauce_type = sauce_type
        print('Sauce type set to: ' + self.sauce_type)

# TODO : Add defaults like the Cheese class
class Toppings:
    def __init__(self, toppings_type = None, toppings_amount = None):
        self.toppings_type = "Pepperoni"
        self.toppings_amount = 5
        if toppings_type :
            self.toppings_type = toppings_type
        if toppings_amount :
            self.toppings_amount = toppings_amount
# How do we get the amounts to change with this short cut code? I tried putting t = Toppings(7), 
# t = Toppings('7'), t = toppings_amount(7), t = get.toppings_amount(), t = Toppings(int:7)

    def get_toppings_type(self):
        return self.toppings_type

# Is there a way to make an error message appear if an integer is put into the toppings_type because
# that wouldn't make sense in our scenario.

    def get_toppings_amount(self):
        return self.toppings_amount

    def set_toppings_and_amount(self, toppings_type, toppings_amount):
        self.toppings_amount = toppings_amount
        self.toppings_type = toppings_type
        print('Toppings type set to: ' + self.toppings_type)
        print('Toppings amount set to: ' + str(self.toppings_amount))

# TODO : Add defaults like the Cheese class
# How can you have no dough though?
class Dough:
    def __init__(self, Dough = None):
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

# I have tried a LOT of different ways to have d.get_dough_type() work, but I cannot figure out
# what my error is.

