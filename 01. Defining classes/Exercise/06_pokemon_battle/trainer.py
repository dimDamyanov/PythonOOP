from .pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, new_pokemon: Pokemon):
        if new_pokemon not in self.pokemon:
            self.pokemon.append(new_pokemon)
            return f'Caught {new_pokemon.pokemon_details()}'
        return 'This pokemon is already caught'

    def release_pokemon(self, pokemon_name):
        filtered = [p for p in self.pokemon if p.first_name == pokemon_name]
        if filtered:
            self.pokemon.remove(filtered[0])
            return f'You have released {pokemon_name}'
        return 'Pokemon is not caught'

    def trainer_data(self):
        return f'Pokemon Trainer {self.name}\n' + f'Pokemon count {len(self.pokemon)}' + ''.join(
            ['\n- ' + p.pokemon_details() + '\n' for p in self.pokemon])
