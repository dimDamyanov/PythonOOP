from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    room_cost = 30

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        super().__init__(family_name, salary_one + salary_two, 2 + len(children))
        self.children = [child for child in children]
        self.appliances = [x for x in [TV(), Fridge(), Laptop()] for _ in range(2 + len(self.children))]
        self.calculate_expenses(self.appliances, self.children)
