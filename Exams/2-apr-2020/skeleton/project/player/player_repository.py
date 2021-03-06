#player_repository.py

class PlayerRepository:
    def __init__(self):
        self.count = 0
        self.players = []

    def add(self, player):
        if player.username in [p.username for p in self.players]:
            raise ValueError(f'Player {player.username} already exists!')
        self.players.append(player)
        self.count += 1

    def remove(self, player: str):
        if player == '':
            raise ValueError('Player cannot be an empty string!')
        player_obj = self.find(player)
        self.players.remove(player_obj)
        self.count -= 1

    def find(self, username: str):
        return [player for player in self.players if player.username == username][0]
