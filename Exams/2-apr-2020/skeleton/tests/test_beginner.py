import unittest

from project.player.beginner import Beginner


class TestBeginner(unittest.TestCase):
    def setUp(self) -> None:
        self.beginner = Beginner('Brian')

    def test_init_attrs_set(self) -> None:
        self.assertEqual(self.beginner.username, 'Brian')
        self.assertEqual(self.beginner.health, 50)
        self.assertTrue(hasattr(self.beginner, 'card_repository'))

    def test_init__when_username_invalid__expect_exception(self) -> None:
        with self.assertRaises(ValueError) as context:
            Beginner('')

        self.assertEqual(context.exception.args[0], 'Player\'s username cannot be an empty string.')

    def test_take_damage__when_damage_valid(self) -> None:
        beginner = Beginner('Bryan')
        beginner.take_damage(25)
        self.assertEqual(beginner.health, 25)

    def test_take_damage__when_damage_invalid__expect_exception(self) -> None:
        with self.assertRaises(ValueError) as context:
            self.beginner.take_damage(-100)

        self.assertEqual(context.exception.args[0], 'Damage points cannot be less than zero.')

    def test_set_health_invalid__expect_exception(self) -> None:
        with self.assertRaises(ValueError) as context:
            self.beginner.health = -100

        self.assertEqual(context.exception.args[0], 'Player\'s health bonus cannot be less than zero.')

    def test_is_dead_property(self) -> None:
        self.beginner.take_damage(50)
        self.assertEqual(self.beginner.is_dead, True)


if __name__ == '__main__':
    unittest.main()
