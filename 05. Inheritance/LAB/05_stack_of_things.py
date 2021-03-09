class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        if isinstance(item, str):
            self.data.insert(0, item)

    def pop(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]

    def is_empty(self):
        return not self.data

    def __str__(self):
        return '[' + ', '.join(self.data) + ']'


