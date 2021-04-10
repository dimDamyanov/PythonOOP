import unittest
from project.battle_field import BattleField
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard


class TestBattleField(unittest.TestCase):
    def setUp(self) -> None:
        self.battle_field = BattleField()
        self.player1 = Advanced('John')
        self.player2 = Beginner('Mike')
        self.player1.card_repository.add(MagicCard('MagicCard1'))
        self.player1.card_repository.add(TrapCard('TrapCard1'))
        self.player2.card_repository.add(MagicCard('MagicCard2'))
        self.player2.card_repository.add(TrapCard('TrapCard2'))

    def test_fight_method(self) -> None:
        self.battle_field.fight(self.player1, self.player2)
        self.assertEqual(self.player1.health, 150)
        self.assertEqual(self.player2.health, 50)


if __name__ == '__main__':
    unittest.main()
