from .player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f'Player {player.name} is already in the guild.'
        if player.guild != 'Unaffiliated':
            return f'Player {player.name} is in another guild.'
        else:
            player.guild = self.name
            self.players.append(player)
            return f'Welcome player {player.name} to the guild {self.name}'

    def kick_player(self, player_name: str):
        for i in range(len(self.players)):
            if self.players[i].first_name == player_name:
                self.players[i].guild = 'Unaffiliated'
                self.players.remove(self.players[i])

                return f'Player {player_name} has been removed from the guild.'
        return f'Player {player_name} is not in the guild.'

    def guild_info(self):
        return f'Guild: {self.name}\n' + '\n'.join([player.player_info() for player in self.players])