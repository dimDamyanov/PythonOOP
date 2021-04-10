import unittest
from project.controller import Controller
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard


class TestBattleField(unittest.TestCase):
    def initialize_players_with_cards(self) -> None:
        self.controller.add_player('Beginner', 'John')
        self.controller.add_player('Advanced', 'Mike')
        self.controller.add_card('Magic', 'MagicCard1')
        self.controller.add_card('Magic', 'MagicCard2')
        self.controller.add_card('Trap', 'TrapCard1')
        self.controller.add_card('Trap', 'TrapCard2')
        self.controller.add_player_card('John', 'MagicCard1')
        self.controller.add_player_card('John', 'TrapCard1')
        self.controller.add_player_card('Mike', 'MagicCard2')
        self.controller.add_player_card('Mike', 'TrapCard2')

    def setUp(self) -> None:
        self.controller = Controller()

    def test_init_attrs_set(self) -> None:
        self.assertEqual(self.controller.player_repository.count, 0)
        self.assertEqual(self.controller.player_repository.players, [])
        self.assertEqual(self.controller.card_repository.count, 0)
        self.assertEqual(self.controller.card_repository.cards, [])

    def test_add_beginner_player(self) -> None:
        msg = self.controller.add_player('Beginner', 'John')
        self.assertEqual(msg, 'Successfully added player of type Beginner with username: John')
        self.assertEqual(self.controller.player_repository.count, 1)
        self.assertEqual(self.controller.player_repository.players[0].username, 'John')
        self.assertTrue(isinstance(self.controller.player_repository.players[0], Beginner))

    def test_add_advanced_player(self) -> None:
        msg = self.controller.add_player('Advanced', 'John')
        self.assertEqual(msg, 'Successfully added player of type Advanced with username: John')
        self.assertEqual(self.controller.player_repository.players[0].username, 'John')
        self.assertTrue(isinstance(self.controller.player_repository.players[0], Advanced))

    def test_add_card_magic(self) -> None:
        msg = self.controller.add_card('Magic', 'Card')
        self.assertEqual(msg, 'Successfully added card of type MagicCard with name: Card')
        self.assertEqual(self.controller.card_repository.count, 1)
        self.assertEqual(self.controller.card_repository.cards[0].name, 'Card')
        self.assertTrue(isinstance(self.controller.card_repository.cards[0], MagicCard))

    def test_add_card_trap(self) -> None:
        msg = self.controller.add_card('Trap', 'Card')
        self.assertEqual(msg, 'Successfully added card of type TrapCard with name: Card')
        self.assertEqual(self.controller.card_repository.count, 1)
        self.assertEqual(self.controller.card_repository.cards[0].name, 'Card')
        self.assertTrue(isinstance(self.controller.card_repository.cards[0], TrapCard))

    def test_add_player_card(self) -> None:
        self.controller.add_card('Magic', 'Card')
        self.controller.add_player('Beginner', 'John')
        msg = self.controller.add_player_card('John', 'Card')
        self.assertEqual(msg, 'Successfully added card: Card to user: John')
        self.assertEqual(self.controller.player_repository.find('John').card_repository.count, 1)
        self.assertEqual(self.controller.player_repository.find('John').card_repository.cards[0].name, 'Card')
        self.assertTrue(isinstance(self.controller.player_repository.find('John').card_repository.cards[0], MagicCard))

    def test_fight_method(self) -> None:
        self.initialize_players_with_cards()
        msg = self.controller.fight('John', 'Mike')
        self.assertEqual(msg, 'Attack user health 50 - Enemy user health 150')

    def test_report_method(self) -> None:
        self.initialize_players_with_cards()
        self.assertEqual(self.controller.report(),
                         'Username: John - Health: 50 - Cards 2\n### Card: MagicCard1 - Damage: 5\n### Card: TrapCard1 - Damage: 120\nUsername: Mike - Health: 250 - Cards 2\n### Card: MagicCard2 - Damage: 5\n### Card: TrapCard2 - Damage: 120\n')


if __name__ == '__main__':
    unittest.main()