from .worker import Worker

import unittest


class WorkerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.worker = Worker('Pesho', 100, 2)

    def test_worker__correct_initialization(self) -> None:
        self.assertEqual(self.worker.name, 'Pesho')
        self.assertEqual(self.worker.salary, 100)
        self.assertEqual(self.worker.energy, 2)

    def test_worker__when_rest__expect_increment_energy(self) -> None:
        self.worker.rest()
        self.assertEqual(self.worker.energy, 3)

    def test_worker__when_work_without_energy__expect_exception(self) -> None:
        self.worker.energy = 0
        with self.assertRaises(Exception):
            self.worker.work()
        self.worker.energy = -1
        with self.assertRaises(Exception):
            self.worker.work()

    def test_increase_salary(self) -> None:
        self.worker.work()
        self.assertEqual(self.worker.money, 100)

    def test_decrease_energy(self) -> None:
        self.worker.work()
        self.assertEqual(self.worker.energy, 1)

    def test_get_info_method(self) -> None:
        self.assertEqual(self.worker.get_info(), 'Pesho has saved 0 money.')


if __name__ == '__main__':
    unittest.main()