from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self, name, weight, food_eaten):
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten

    @abstractmethod
    def make_sound(self):
        pass


class Bird(ABC, Animal):
    @abstractmethod
    def __init__(self, name, weight, food_eaten, wing_size):
        super(Bird, self).__init__(name, weight, food_eaten)
        self.wing_size = wing_size

    def __repr__(self):
        return f'{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]'


class Mammal(ABC, Animal):
    @abstractmethod
    def __init__(self, name, weight, food_eaten, living_region):
        super(Mammal, self).__init__(name, weight, food_eaten)
        self.living_region = living_region

    def __repr__(self):
        return f'{self.__class__.__name__} [{self.name}, {self.living_region}, {self.weight}, {self.food_eaten}]'