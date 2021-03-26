import unittest

from ..project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(50, 200)

    def test_init_attributes_set__expect_valid_attributes(self) -> None:
        self.assertEqual(self.vehicle.fuel, 50)
        self.assertEqual(self.vehicle.horse_power, 200)
        self.assertEqual(self.vehicle.capacity, 50)
        self.assertEqual(self.vehicle.fuel_consumption, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive__when_fuel_is_not_enough__expect_exception(self) -> None:
        with self.assertRaises(Exception) as context:
            self.vehicle.drive(44)
        self.assertEqual(context.exception.args[0], 'Not enough fuel')

    def test_drive__when_fuel_is_enough_expect_fuel_decrease(self) -> None:
        self.vehicle.drive(16)
        self.assertEqual(self.vehicle.fuel, 30)

    def test_refuel__when_fuel_is_overloaded__expect_exception(self) -> None:
        with self.assertRaises(Exception) as context:
            self.vehicle.refuel(1)
        self.assertEqual(context.exception.args[0], 'Too much fuel')

    def test_refuel__when_fuel_is_not_overloaded__expect_fuel_increase(self) -> None:
        self.vehicle.fuel = 0
        self.vehicle.refuel(25)
        self.assertEqual(self.vehicle.fuel, 25)

    def test_str_representation_method(self) -> None:
        self.assertEqual(str(self.vehicle),
                         f"The vehicle has 200 horse power with 50 fuel left and 1.25 fuel consumption")


if __name__ == '__main__':
    unittest.main()
