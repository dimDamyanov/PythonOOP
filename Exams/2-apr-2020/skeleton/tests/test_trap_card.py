import unittest
from project.card.trap_card import TrapCard


class TestTrapCard(unittest.TestCase):
    def setUp(self) -> None:
        self.trap_card = TrapCard('Card')

    def test_init_attrs_set(self) -> None:
        self.assertEqual(self.trap_card.name, 'Card')
        self.assertEqual(self.trap_card.damage_points, 120)
        self.assertEqual(self.trap_card.health_points, 5)

    def test_init__when_name_invalid__expect_exception(self) -> None:
        with self.assertRaises(ValueError) as context:
            TrapCard('')

        self.assertEqual(context.exception.args[0], 'Card\'s name cannot be an empty string.')

    def test_damage_points_setter__expect_exception(self) -> None:
        with self.assertRaises(ValueError) as context:
            self.trap_card.damage_points = -10

        self.assertEqual(context.exception.args[0], 'Card\'s damage points cannot be less than zero.')

    def test_health_points_setter__expect_exception(self) -> None:
        with self.assertRaises(ValueError) as context:
            self.trap_card.health_points = -10

        self.assertEqual(context.exception.args[0], 'Card\'s HP cannot be less than zero.')


if __name__ == '__main__':
    unittest.main()
