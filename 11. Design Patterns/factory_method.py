import json
from abc import ABC, abstractmethod


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Parser(ABC):
    @abstractmethod
    def parse(self, obj):
        pass


class JsonParser(Parser):
    def parse(self, obj):
        return json.dumps(obj.__dict__)


class CSVParser(Parser):
    def parse(self, obj):
        result = [','.join(obj.__dict__.keys()),
                  ','.join(str(x) for x in obj.__dict__.values())
                  ]
        return '\n'.join(result)


class StringParser(Parser):
    def parse(self, obj):
        return str(obj)


class ParsersFactory:
    def get(self, format) -> Parser:
        if format == 'json':
            return JsonParser()
        elif format == 'csv':
            return CSVParser()
        else:
            return StringParser()


pesho = Person('Pesho', 11)
parsers_factory = ParsersFactory()

format = input()
parser = parsers_factory.get(format)
result = parser.parse(pesho)
print(result)
