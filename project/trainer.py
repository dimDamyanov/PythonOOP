class Trainer:
    current_id = 0

    def __init__(self, name: str):
        self.id = self.get_next_id()
        self.name = name

    def __repr__(self):
        return f'Trainer <{self.id}> {self.name}'

    @staticmethod
    def get_next_id():
        Trainer.current_id += 1
        return Trainer.current_id
