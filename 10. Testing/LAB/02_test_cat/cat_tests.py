from .cat import Cat

import unittest


class CatTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cat = Cat('Felix')

    def test_cat__when_fed__expect_size_increase(self) -> None:
        self.cat.eat()
        self.assertEqual(self.cat.size, 1)

    def test_cat__when_fed__expect_fed_true(self) -> None:
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cat__eat_when_fed_true__expect_exception(self) -> None:
        self.cat.fed = True
        with self.assertRaises(Exception):
            self.cat.eat()

    def test_cat__sleep_when_fed_true__expect_exception(self) -> None:
        with self.assertRaises(Exception):
            self.cat.sleep()

    def test_cat__sleepy_after_sleep__expect_sleepy_false(self) -> None:
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    unittest.main()
