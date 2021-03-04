class Person:
    MIN_AGE = 0
    MAX_AGE = 150

    def __init__(self, first_name, last_name, age, city=None):
        self.first_name = first_name
        self.last_name = last_name
        self.set_age(age)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, new_name):
        if not new_name:
            raise ValueError('Name cannot be None')
        self.__first_name = new_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, new_name):
        self.__last_name = new_name

    def set_age(self, new_age):
        if new_age < Person.MIN_AGE or Person.MAX_AGE < new_age:
            raise ValueError(f'Age must be between {Person.MIN_AGE} and {Person.MAX_AGE}')
        self.__age = new_age

    def get_age(self):
        return self.__age

    # def __setattr__(self, key, value):
    #     if len(key) > 1 and key.startswith('_') and key[1] != '_':
    #         key = f'_{self.__class__.__name__}${key}'
    #     return super().__setattr__(key, value)
    #
    # def __getattr__(self, item):
    #     if len(item) > 1 and item.startswith('_') and item[1] != '_':
    #         item = f'_{self.__class__.__name__}${item}'
    #     return super().__getattribute__(item)


pesho = Person('Pesho', 'Ivanov',  1)
print(pesho.__dict__)
print(pesho.full_name)
pesho.first_name = 'Ivan'
pesho.last_name = 'Peshov'
print(pesho.__dict__)
print(pesho.full_name)