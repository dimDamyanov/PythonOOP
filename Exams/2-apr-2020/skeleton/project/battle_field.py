#battle_field.py

from project.player.player import Player


class BattleField:
    def fight(self, attacker: Player, enemy: Player):
        if attacker.is_dead or enemy.is_dead:
            raise ValueError('Player is dead!')

        for player in (attacker, enemy):
            if player.__class__.__name__ == 'Beginner':
                player.health += 40
                for card in player.card_repository.cards:
                    card.damage_points += 30

            player.health += sum([card.health_points for card in player.card_repository.cards])

        for card in attacker.card_repository.cards:
            if enemy.is_dead:
                return
            enemy.take_damage(card.damage_points)

        for card in enemy.card_repository.cards:
            if attacker.is_dead:
                return
            attacker.take_damage(card.damage_points)
