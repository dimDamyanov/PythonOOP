from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def total_capacity():
        return sum([hardware.capacity for hardware in System._hardware])

    @staticmethod
    def used_capacity():
        return sum([software.capacity_consumption for software in System._software])

    @staticmethod
    def total_memory():
        return sum([hardware.memory for hardware in System._hardware])

    @staticmethod
    def used_memory():
        return sum([software.memory_consumption for software in System._software])

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int,
                                  memory_consumption: int):
        for hardware in System._hardware:
            if hardware.name == hardware_name:
                express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
                try:
                    hardware.install(express_software)
                except Exception as e:
                    return e.args[0]

                System._software.append(express_software)
                return

        return "Hardware does not exist"

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int,
                                memory_consumption: int):
        for hardware in System._hardware:
            if hardware.name == hardware_name:
                light_software = LightSoftware(name, capacity_consumption, memory_consumption)
                try:
                    hardware.install(light_software)
                except Exception as e:
                    return e.args[0]

                System._software.append(light_software)
                return

        return "Hardware does not exist"

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        for hardware in System._hardware:
            if hardware.name == hardware_name:
                for software in hardware.software_components:
                    if software.name == software_name:
                        hardware.uninstall(software)
                        System._software.remove(software)
                        return

        return 'Some of the components do not exist'

    @staticmethod
    def analyze():
        return f'System Analysis\n' \
               f'Hardware Components: {len(System._hardware)}\n' \
               f'Software Components: {len(System._software)}\n' \
               f'Total Operational Memory: {System.used_memory()} / {System.total_memory()}\n' \
               f'Total Capacity Taken: {System.used_capacity()} / {System.total_capacity()}'

    @staticmethod
    def system_split():
        components = [f'Hardware Component - {hardware.name}\n'
                      f'Express Software Components: {hardware.express_software_components_count}\n'
                      f'Light Software Components: {hardware.light_software_components_count}\n'
                      f'Memory Usage: {hardware.used_memory} / {hardware.memory}\n'
                      f'Capacity Usage: {hardware.used_capacity} / {hardware.capacity}\n'
                      f'Type: {hardware.type}\n'
                      f'Software Components: '
                      f'{", ".join([software.name for software in hardware.software_components]) if hardware.software_components else "None"}'
                      for hardware in System._hardware]
        return ''.join(components)
