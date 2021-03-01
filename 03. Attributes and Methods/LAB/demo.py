# class Person:
#     max_age = 150
#
#     def __init__(self, name: str, age: int):
#         self.validate_age(age)
#         self.name = name
#         self.age = age
#
#     @staticmethod
#     def validate_age(age: int):
#         if age < 0 or age > Person.max_age:
#             raise ValueError('Age is invalid')
#
#     @classmethod
#     def is_age_valid(cls, age: int):
#         if not hasattr(cls, 'max_age'):
#             raise TypeError(f'{cls} must have class attribute `max_age`')
#         return 0 <= age <= cls.max_age
#
#     def __repr__(self):
#         return f'{self.name} => {self.age}'
#
#
# print(Person('Gosho', 11))
# print(Person.is_age_valid(5))
# print(Person.is_age_valid(555))
# print(Person('Gosho', 1111))


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __repr__(self):
        return f'radius: ${self.radius}'

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)


print(Circle(5))
print(Circle.from_diameter(10))
