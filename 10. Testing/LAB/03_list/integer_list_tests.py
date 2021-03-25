from .integer_list import IntegerList

import unittest


class IntegerListTests(unittest.TestCase):
    def setUp(self) -> None:
        self.int_list = IntegerList(1, 2, 3, 4, 5)

    def test_add__element_not_integer__expect_value_error(self) -> None:
        with self.assertRaises(ValueError):
            self.int_list.add('str')

    def test_add__valid_element__expect_return_list(self) -> None:
        self.assertEqual(self.int_list.add(6), [1, 2, 3, 4, 5, 6])

    def test_remove_index__index_not_in_range__expect_index_error(self) -> None:
        with self.assertRaises(IndexError):
            self.int_list.remove_index(5)

    def test_remove_index__return_element__expect_removed_element(self) -> None:
        self.assertEqual(self.int_list.remove_index(0), 1)
        self.assertEqual(self.int_list.get_data(), [2, 3, 4, 5])

    def test__init__other_types_involved__expect_only_integers(self) -> None:
        self.int_list = IntegerList(1, 'two', 3, 'four', 5)
        self.assertEqual(self.int_list.get_data(), [1, 3, 5])

    def test_get__index_not_in_range__expect_index_error(self) -> None:
        with self.assertRaises(IndexError):
            self.int_list.get(5)

    def test_insert__index_not_in_range__expect_index_error(self) -> None:
        with self.assertRaises(IndexError):
            self.int_list.insert(5, 6)

    def test_insert__element_not_integer__expect_value_error(self) -> None:
        with self.assertRaises(ValueError):
            self.int_list.insert(0, 'zero')

    def test_insert__element_valid__expect_change_in_list(self) -> None:
        self.int_list.insert(0, 0)
        self.assertEqual(self.int_list.get_data(), [0, 1, 2, 3, 4, 5])

    def test_get_biggest(self) -> None:
        self.assertEqual(self.int_list.get_biggest(), 5)

    def test_get_index(self) -> None:
        self.assertEqual(self.int_list.get_index(2), 1)


if __name__ == '__main__':
    unittest.main()
