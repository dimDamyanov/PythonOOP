class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f'Hello, my name is {self.name}')


class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def say_hello(self):
        super().say_hello()
        print(f'My salary is {self.salary}')


pesho = Employee("Pesho", 1000)
pesho.say_hello()