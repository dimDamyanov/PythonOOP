from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository: DecorationRepository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type == 'FreshwaterAquarium':
            self.aquariums.append(FreshwaterAquarium(aquarium_name))
            return f'Successfully added {aquarium_type}.'
        elif aquarium_type == 'SaltwaterAquarium':
            self.aquariums.append(SaltwaterAquarium(aquarium_name))
            return f'Successfully added {aquarium_type}.'
        else:
            return 'Invalid aquarium type.'

    def add_decoration(self, decoration_type: str):
        if decoration_type == 'Ornament':
            self.decorations_repository.add(Ornament())
            return f'Successfully added {decoration_type}.'
        elif decoration_type == 'Plant':
            self.decorations_repository.add(Plant())
            return f'Successfully added {decoration_type}.'
        else:
            return 'Invalid decoration type.'

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        decoration = self.decorations_repository.find_by_type(decoration_type)
        if aquarium_name in [aquarium.name for aquarium in self.aquariums] and decoration != "None":
            aquarium = [aquarium for aquarium in self.aquariums if aquarium.name == aquarium_name][0]
            aquarium.add_decoration(decoration)
            self.decorations_repository.remove(decoration)
            return f'Successfully added {decoration_type} to {aquarium_name}.'
        else:
            return f'There isn\'t a decoration of type {decoration_type}.'

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        aquarium = [aquarium for aquarium in self.aquariums if aquarium.name == aquarium_name][0]
        if fish_type == 'FreshwaterFish':
            fish = FreshwaterFish(fish_name, fish_species, price)
            return aquarium.add_fish(fish)
        elif fish_type == 'SaltwaterFish':
            fish = SaltwaterFish(fish_name, fish_species, price)
            return aquarium.add_fish(fish)
        else:
            return f'There isn\'t a fish of type {fish_type}.'

    def feed_fish(self, aquarium_name: str):
        aquarium = [aquarium for aquarium in self.aquariums if aquarium.name == aquarium_name][0]
        aquarium.feed()
        return f'Fish fed: {len(aquarium.fish)}'

    def calculate_value(self, aquarium_name: str):
        aquarium = [aquarium for aquarium in self.aquariums if aquarium.name == aquarium_name][0]
        value = sum([fish.price for fish in aquarium.fish])
        value += sum([decoration.price for decoration in aquarium.decorations])
        return f'The value of Aquarium {aquarium_name} is {value:.2f}.'

    def report(self):
        return '\n'.join([str(aquarium) for aquarium in self.aquariums])
