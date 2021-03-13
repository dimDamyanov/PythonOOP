from project1.dough import Dough
from project1.topping import Topping


class Pizza:
    def __init__(self, name: str, dough: Dough, toppings_capacity: int):
        self.__name = name
        self.__dough = dough
        self.__toppings_capacity = toppings_capacity
        self.__toppings = {}

    def add_topping(self, topping: Topping):
        if len(self.__toppings) < self.__toppings_capacity:
            if topping.topping_type not in self.__toppings:
                self.__toppings[topping.topping_type] = topping.weight
            else:
                self.__toppings[topping.topping_type] += topping.weight
        else:
            raise ValueError("Not enough space for another topping")

    def calculate_total_weight(self):
        return self.__dough.weight + sum(self.__toppings.values())

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        self.__dough = value

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        self.__toppings_capacity = value

    @property
    def toppings(self):
        return self.__toppings

    @toppings.setter
    def toppings(self, value):
        self.__toppings = value
