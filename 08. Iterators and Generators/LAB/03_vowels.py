class vowels:
    def __init__(self, string):
        self.string = string
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.string):
            raise StopIteration
        ch = self.string[self.index]
        self.index += 1
        if not ch.casefold() in {'a', 'e', 'i', 'o', 'u', 'y'}:
            return self.__next__()
        return ch


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
