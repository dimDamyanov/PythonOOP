class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'{self.name}; {self.age}'


def get_object_by_attr_value(objects, **kwargs):
    result = set()
    for obj in objects:
        is_valid = True
        for key, value in kwargs.items():
            if not hasattr(obj, key) or getattr(obj, key, None) != value:
                is_valid = False
                break
            if is_valid:
                result.add(obj)
    return result


people = [
    Person('Pesho', 11),
    Person('Gosho', 11)
]

print(get_object_by_attr_value(people, age=11))
