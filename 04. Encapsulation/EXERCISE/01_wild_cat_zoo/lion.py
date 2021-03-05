class Lion:
    __NEED = 50

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    @classmethod
    def get_needs(cls):
        return cls.__NEED

    def __repr__(self):
        return f'Name: {self.name}, Age: {self.age}, Gender: {self.gender}'
