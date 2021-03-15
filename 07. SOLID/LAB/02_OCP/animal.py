from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def get_sound(self):
        pass


class Dog(Animal):
    def get_sound(self):
        return 'woof-woof'


class Cat(Animal):
    def get_sound(self):
        return 'meow'


class Chicken(Animal):
    def get_sound(self):
        return 'cluck'


animals = [Dog(), Cat(), Chicken()]
[print(animal.get_sound()) for animal in animals]
