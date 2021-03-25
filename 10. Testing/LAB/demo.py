import unittest


def validate_type(value, types):
    if type(value) not in types:
        raise ValueError('`numbers` should be numbers')

def my_sum(numbers):
    [validate_type(x, (int, float)) for x in numbers]
    return sum(numbers)


class SampleTests(unittest.TestCase):
    def setUp(self) -> None:
        print('Running')

    @classmethod
    def setUpClass(cls) -> None:
        print('SetUpClass')

    def test_my_sum_when_ints_are_equal(self):
        numbers = [1, 2, 3, 4]
        actual_result = my_sum(numbers)
        expected_result = 10
        self.assertEqual(expected_result, actual_result)

    @classmethod
    def tearDownClass(cls) -> None:
        print('TearDownClass')

    def tearDown(self) -> None:
        print('tearDown')

    def test_my_sum_when_floats_are_equal(self):
        numbers = [1.0, 2.0, 3.0, 4.0]
        actual_result = my_sum(numbers)
        expected_result = 10
        self.assertEqual(expected_result, actual_result)

    def test_my_sum_when_strings(self):
        numbers = ['a', 'b', 'c']
        with self.assertRaises(ValueError) as context:
            my_sum(numbers)

        self.assertEqual('`numbers` should be numbers', context.exception.args[0])
