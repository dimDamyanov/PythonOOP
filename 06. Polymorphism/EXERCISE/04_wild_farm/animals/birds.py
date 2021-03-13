from .animal import Bird
from ..food import Meat, Food


class Owl(Bird):
    WEIGHT_INCREASE = 0.25

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food: Food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += Owl.WEIGHT_INCREASE * food.quantity
        self.food_eaten += food.quantity


class Hen(Bird):
    WEIGHT_INCREASE = 0.35

    def make_sound(self):
        return "Cluck"

    def feed(self, food: Food):
        self.weight += Hen.WEIGHT_INCREASE * food.quantity
        self.food_eaten += food.quantity
