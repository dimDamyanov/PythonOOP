import unittest
from project.hardware.hardware import Hardware
from project.software.software import Software


class TestHardware(unittest.TestCase):
    def setUp(self) -> None:
        self.hardware = Hardware('SSD', 'Storage', 512, 128)

    def test_init_method__expect_correct_initialization(self) -> None:
        self.assertEqual(self.hardware.name, 'SSD')
        self.assertEqual(self.hardware.type, 'Storage')
        self.assertEqual(self.hardware.capacity, 512)
        self.assertEqual(self.hardware.memory, 128)
        self.assertEqual(self.hardware.software_components, [])

    def test_install__when_capacity_valid_and_memory_valid__expect_software_installed(self) -> None:
        software = Software('Manjaro', 'OS', 256, 64)
        self.hardware.install(software)
        self.assertEqual(self.hardware.software_components, [software])

    def test_install__when_capacity_invalid_and_memory_valid__expect_exception(self) -> None:
        software = Software('Manjaro', 'OS', 1024, 64)
        with self.assertRaises(Exception) as context:
            self.hardware.install(software)

        self.assertEqual(context.exception.args[0], 'Software cannot be installed')

    def test_install__when_capacity_valid_and_memory_invalid__expect_exception(self) -> None:
        software = Software('Manjaro', 'OS', 256, 256)
        with self.assertRaises(Exception) as context:
            self.hardware.install(software)

        self.assertEqual(context.exception.args[0], 'Software cannot be installed')

    def test_install__when_capacity_invalid_and_memory_invalid__expect_exception(self) -> None:
        software = Software('Manjaro', 'OS', 1024, 256)
        with self.assertRaises(Exception) as context:
            self.hardware.install(software)

        self.assertEqual(context.exception.args[0], 'Software cannot be installed')

    def test_uninstall__expect_software_uninstalled(self) -> None:
        software = Software('Manjaro', 'OS', 256, 64)
        self.hardware.install(software)
        self.hardware.uninstall(software)
        self.assertEqual(self.hardware.software_components, [])


if __name__ == '__main__':
    unittest.main()
