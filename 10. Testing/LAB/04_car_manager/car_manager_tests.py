from .car_manager import Car

import unittest


class CarTests(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car('Audi', 'S6', 6.3, 75)

    def test_init__expect_correct_data(self) -> None:
        self.assertEqual(self.car.make, 'Audi')
        self.assertEqual(self.car.model, 'S6')
        self.assertEqual(self.car.fuel_consumption, 6.3)
        self.assertEqual(self.car.fuel_capacity, 75)

    def test_init__when_make_empty__expect_exception(self) -> None:
        with self.assertRaises(Exception):
            self.car.make = ''

    def test_init__when_model_empty__expect_exception(self) -> None:
        with self.assertRaises(Exception):
            self.car.model = ''

    def test_init__when_fuel_consumption_is_negative_or_zero__expect_exception(self) -> None:
        with self.assertRaises(Exception):
            self.car.fuel_consumption = 0
        with self.assertRaises(Exception):
            self.car.fuel_consumption = -1

    def test_init__when_fuel_capacity_is_negative_or_zero__expect_exception(self) -> None:
        with self.assertRaises(Exception):
            self.car.fuel_capacity = 0
        with self.assertRaises(Exception):
            self.car.fuel_capacity = -1

    def test_init__when_fuel_amount_is_negative__expect_exception(self) -> None:
        with self.assertRaises(Exception):
            self.car.fuel_amount = -1

    def test_refuel__when_fuel_is_negative_or_zero__expect_exception(self) -> None:
        with self.assertRaises(Exception):
            self.car.refuel(0)
        with self.assertRaises(Exception):
            self.car.refuel(-1)

    def test_refuel__when_fuel_is_greater_than_fuel_capacity__expect_fuel_capacity(self) -> None:
        self.car.refuel(80)
        self.assertEqual(self.car.fuel_amount, 75)

    def test_refuel__when_fuel_is_correct__expect_fuel(self) -> None:
        self.car.refuel(50)
        self.assertEqual(self.car.fuel_amount, 50)

    def test_drive__when_distance_is_greater_than_possible__expect_exception(self) -> None:
        self.car.fuel_amount = 6.3
        with self.assertRaises(Exception):
            self.car.drive(150)

    def test_drive__when_distance_is_possible__expect_fuel_drop(self) -> None:
        self.car.fuel_amount = 12.6
        self.car.drive(100)
        self.assertEqual(self.car.fuel_amount, 6.3)


if __name__ == '__main__':
    unittest.main()
