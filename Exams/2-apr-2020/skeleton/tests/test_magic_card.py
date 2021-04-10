import unittest
from project.card.magic_card import MagicCard


class TestMagicCard(unittest.TestCase):
    def setUp(self) -> None:
        self.magic_card = MagicCard('Card')

    def test_init_attrs_set(self) -> None:
        self.assertEqual(self.magic_card.name, 'Card')
        self.assertEqual(self.magic_card.damage_points, 5)
        self.assertEqual(self.magic_card.health_points, 80)

    def test_init__when_name_invalid__expect_exception(self) -> None:
        with self.assertRaises(ValueError) as context:
            MagicCard('')

        self.assertEqual(context.exception.args[0], 'Card\'s name cannot be an empty string.')

    def test_damage_points_setter__expect_exception(self) -> None:
        with self.assertRaises(ValueError) as context:
            self.magic_card.damage_points = -10

        self.assertEqual(context.exception.args[0], 'Card\'s damage points cannot be less than zero.')

    def test_health_points_setter__expect_exception(self) -> None:
        with self.assertRaises(ValueError) as context:
            self.magic_card.health_points = -10

        self.assertEqual(context.exception.args[0], 'Card\'s HP cannot be less than zero.')


if __name__ == '__main__':
    unittest.main()
