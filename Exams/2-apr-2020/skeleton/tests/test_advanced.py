import unittest

from project.player.advanced import Advanced


class TestAdvanced(unittest.TestCase):
    def setUp(self) -> None:
        self.advanced = Advanced('Brian')

    def test_init_attrs_set(self) -> None:
        self.assertEqual(self.advanced.username, 'Brian')
        self.assertEqual(self.advanced.health, 250)
        self.assertTrue(hasattr(self.advanced, 'card_repository'))

    def test_init__when_username_invalid__expect_exception(self) -> None:
        with self.assertRaises(ValueError) as context:
            Advanced('')

        self.assertEqual(context.exception.args[0], 'Player\'s username cannot be an empty string.')

    def test_take_damage__when_damage_valid(self) -> None:
        advanced = Advanced('Bryan')
        advanced.take_damage(100)
        self.assertEqual(advanced.health, 150)

    def test_take_damage__when_damage_invalid__expect_exception(self) -> None:
        with self.assertRaises(ValueError) as context:
            self.advanced.take_damage(-100)

        self.assertEqual(context.exception.args[0], 'Damage points cannot be less than zero.')

    def test_set_health_invalid__expect_exception(self) -> None:
        with self.assertRaises(ValueError) as context:
            self.advanced.health = -100

        self.assertEqual(context.exception.args[0], 'Player\'s health bonus cannot be less than zero.')

    def test_is_dead_property(self) -> None:
        self.advanced.take_damage(250)
        self.assertEqual(self.advanced.is_dead, True)


if __name__ == '__main__':
    unittest.main()
