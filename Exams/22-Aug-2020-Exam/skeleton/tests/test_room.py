import unittest

from project.rooms.room import Room


class Appliance:
    def __init__(self, cost: float):
        self.cost = cost

    def get_monthly_expense(self):
        return self.cost * 30


class TestRoom(unittest.TestCase):
    def setUp(self) -> None:
        self.room = Room('Lindemann', 450, 1)

    def test_init__expect_attrs_set(self) -> None:
        self.assertEqual(self.room.family_name, 'Lindemann')
        self.assertEqual(self.room.budget, 450)
        self.assertEqual(self.room.members_count, 1)
        self.assertEqual(self.room.children, [])
        self.assertTrue(hasattr(self.room, 'expenses'))

    def test_setter_expenses__when_valid__expect_expenses_updates(self) -> None:
        self.room.expenses = 45
        self.assertEqual(self.room.expenses, 45)

    def test_setter_expenses__when_invalid__expect_exception(self) -> None:
        with self.assertRaises(ValueError) as context:
            self.room.expenses = -30

        self.assertEqual(context.exception.args[0], 'Expenses cannot be negative')

    def test_calculate_expenses(self) -> None:
        appliances = [Appliance(10), Appliance(8)]
        appliances1 = [Appliance(8), Appliance(10)]
        self.room.calculate_expenses(appliances, appliances1)

        self.assertEqual(self.room.expenses, 1080)
