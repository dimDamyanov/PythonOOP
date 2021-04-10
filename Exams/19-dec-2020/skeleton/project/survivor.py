class Survivor:
    MAX_HEALTH = 100
    MAX_NEEDS = 100

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.needs = Survivor.MAX_NEEDS
        self.health = Survivor.MAX_HEALTH

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError('Name not valid!')
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError('Age not valid!')
        self.__age = value

    @property
    def needs(self):
        return self.__needs

    @needs.setter
    def needs(self, value):
        if value < 0:
            raise ValueError('Needs not valid!')
        elif value >= Survivor.MAX_NEEDS:
            self.__needs = Survivor.MAX_NEEDS
            return

        self.__needs = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            raise ValueError('Health not valid!')
        elif value >= Survivor.MAX_HEALTH:
            self.__health = Survivor.MAX_HEALTH
            return

        self.__health = value

    @property
    def needs_sustenance(self):
        return self.needs < 100

    @property
    def needs_healing(self):
        return self.health < 100
