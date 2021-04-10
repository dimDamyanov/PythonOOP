from project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):
    def __init__(self, name: str):
        super().__init__(name, 50)

    def add_fish(self, fish):
        if fish.__class__.__name__ == 'FreshwaterFish':
            return super().add_fish(fish)
        else:
            return 'Water not suitable.'
