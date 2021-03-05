class Equipment:
    id = 0

    def __init__(self, name: str):
        self.id = self.get_next_id()
        Equipment.id += 1
        self.name = name

    def __repr__(self):
        return f'Equipment <{self.id}> {self.name}'

    @staticmethod
    def get_next_id():
        return Equipment.id
