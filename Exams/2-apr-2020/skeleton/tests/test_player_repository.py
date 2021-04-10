import unittest
from project.player.player_repository import PlayerRepository
from project.player.advanced import Advanced


class TestPlayerRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.player_repository = PlayerRepository()

    def test_init__attrs_set(self) -> None:
        self.assertListEqual(self.player_repository.players, [])
        self.assertEqual(self.player_repository.count, 0)

    def test_add__when_player_valid(self) -> None:
        player = Advanced('John')
        self.player_repository.add(player)
        self.assertEqual(self.player_repository.count, 1)
        self.assertListEqual(self.player_repository.players, [player])

    def test_add__when_player_invalid(self) -> None:
        player1 = Advanced('John')
        player2 = Advanced('John')
        self.player_repository.add(player1)
        with self.assertRaises(ValueError) as context:
            self.player_repository.add(player2)

        self.assertEqual(context.exception.args[0], 'Player John already exists!')

    def test_remove__when_player_valid(self) -> None:
        player = Advanced('John')
        self.player_repository.add(player)
        self.player_repository.remove('John')
        self.assertEqual(self.player_repository.count, 0)
        self.assertListEqual(self.player_repository.players, [])

    def test_remove__when_player_invalid__expect_exception(self) -> None:
        player = Advanced('John')
        self.player_repository.add(player)
        with self.assertRaises(ValueError) as context:
            self.player_repository.remove('')

        self.assertEqual(context.exception.args[0], 'Player cannot be an empty string!')

    def test_find_method(self) -> None:
        player = Advanced('John')
        self.player_repository.add(player)
        self.assertEqual(self.player_repository.find('John'), player)


if __name__ == '__main__':
    unittest.main()
