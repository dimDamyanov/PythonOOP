from ..project.mammal import Mammal

import unittest


class MammalTests(unittest.TestCase):

    def setUp(self):
        self.mammal = Mammal('Muki', 'Animal', 'Muuuuuuu')

    def test_name(self):
        result = self.mammal.name
        expected_result = 'Muki'
        self.assertEqual(result, expected_result)

    def test_type(self):
        result = self.mammal.type
        expected_result = 'Animal'
        self.assertEqual(result, expected_result)

    def test_sound(self):
        result = self.mammal.sound
        expected_result = 'Muuuuuuu'
        self.assertEqual(result, expected_result)

    def test_make_sound_method(self):
        result = self.mammal.make_sound()
        expected_result = "Muki makes Muuuuuuu"
        self.assertEqual(result, expected_result)

    def test_kingdom_initial(self):
        result = self.mammal._Mammal__kingdom
        expected_result = "animals"
        self.assertEqual(result, expected_result)

    def test_get_kingdom_method(self):
        result = self.mammal.get_kingdom()
        expected_result = "animals"
        self.assertEqual(result, expected_result)

    def test_info_method(self):
        result = self.mammal.info()
        expected_result = "Muki is of type Animal"
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
