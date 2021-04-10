import unittest
from project.factory.paint_factory import PaintFactory


class TestPaintFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.paint_factory = PaintFactory('TestName', 10)

    def test_init__expect_attrs_set(self) -> None:
        self.assertEqual(self.paint_factory.name, 'TestName')
        self.assertEqual(self.paint_factory.capacity, 10)
        self.assertEqual(self.paint_factory.ingredients, {})

    def test_add_ingredient__when_valid_enough_space__expect_added(self) -> None:
        self.paint_factory.add_ingredient('white', 5)
        self.assertEqual(self.paint_factory.ingredients, {'white': 5})
        self.paint_factory.add_ingredient('white', 3)
        self.assertEqual(self.paint_factory.ingredients, {'white': 8})

    def test_add_ingredient__when_valid_not_enough_space__expect_exception(self) -> None:
        with self.assertRaises(ValueError) as context:
            self.paint_factory.add_ingredient('white', 15)

        self.assertEqual(context.exception.args[0], 'Not enough space in factory')

    def test_add_ingredient__when_invalid__expect_exception(self) -> None:
        with self.assertRaises(TypeError) as context:
            self.paint_factory.add_ingredient('purple', 5)

        self.assertEqual(context.exception.args[0], 'Ingredient of type purple not allowed in PaintFactory')

    def test_remove_ingredient__when_invalid__expect_exception(self) -> None:
        with self.assertRaises(KeyError) as context:
            self.paint_factory.remove_ingredient('white', 10)

        self.assertEqual(context.exception.args[0], 'No such ingredient in the factory')

    def test_remove_ingredient__when_valid_enough_quantity(self) -> None:
        self.paint_factory.add_ingredient('white', 8)
        self.paint_factory.remove_ingredient('white', 3)
        self.assertEqual(self.paint_factory.ingredients, {'white': 5})

    def test_remove_ingredient__when_valid_not_enough_quantity__expect_exception(self) -> None:
        self.paint_factory.add_ingredient('white', 5)
        with self.assertRaises(ValueError) as context:
            self.paint_factory.remove_ingredient('white', 10)

        self.assertEqual(context.exception.args[0], 'Ingredients quantity cannot be less than zero')

    def test_property_products(self) -> None:
        self.assertEqual(self.paint_factory.products, {})
        self.paint_factory.add_ingredient('white', 8)
        self.assertEqual(self.paint_factory.products, {'white': 8})

    def test_repr_method(self) -> None:
        self.paint_factory.add_ingredient('white', 5)
        self.paint_factory.add_ingredient('blue', 3)
        self.assertEqual(repr(self.paint_factory), 'Factory name: TestName with capacity 10.\nwhite: 5\nblue: 3\n')


if __name__ == '__main__':
    unittest.main()
