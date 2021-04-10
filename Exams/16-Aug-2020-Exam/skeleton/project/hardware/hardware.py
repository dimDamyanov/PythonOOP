from project.software.software import Software


class Hardware:
    def __init__(self, name: str, type: str, capacity: int, memory: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    @property
    def free_capacity(self):
        return self.capacity - sum([software.capacity_consumption for software in self.software_components])

    @property
    def used_capacity(self):
        return self.capacity - self.free_capacity

    @property
    def free_memory(self):
        return self.memory - sum([software.memory_consumption for software in self.software_components])

    @property
    def used_memory(self):
        return self.memory - self.free_memory

    @property
    def express_software_components_count(self):
        return len([software for software in self.software_components if software.type == 'Express'])

    @property
    def light_software_components_count(self):
        return len([software for software in self.software_components if software.type == 'Light'])

    def install(self, software: Software):
        if self.free_capacity < software.capacity_consumption or self.free_memory < software.memory_consumption:
            raise Exception('Software cannot be installed')

        self.software_components.append(software)

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)
