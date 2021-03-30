# noinspection PyTypeChecker,PyUnresolvedReferences
class HashTable:
    resize_factor = 0.7

    def __init__(self):
        self.count = 0
        self.capacity = 8
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity

    def execute_resize_check(self):
        return self.capacity * self.resize_factor <= self.count

    def get_index(self, key):
        key_hash = hash(key)
        return abs(key_hash) % self.capacity

    def resize(self):
        self.count = 0
        old_keys = self.keys
        old_values = self.values
        self.capacity *= 2
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity
        for key_nested_list, value_nested_list in zip(old_keys, old_values):
            if key_nested_list and value_nested_list:
                for key, value in zip(key_nested_list, value_nested_list):
                    self.add(key, value)

    def __setitem__(self, key, value):
        index = self.get_index(key)
        if not self.keys[index]:
            self.keys[index] = []
            self.values[index] = []
        if key not in self.keys[index]:
            self.keys[index].append(key)
            self.values[index].append(value)
        else:
            internal_index = self.keys[index].index(key)
            self.values[index][internal_index] = value
            return
        self.count += 1
        if self.execute_resize_check():
            self.resize()

    def add(self, key, value):
        self.__setitem__(key, value)

    def __getitem__(self, item):
        index = self.get_index(item)
        if item not in self.keys[index]:
            raise KeyError(item)
        internal_index = self.keys[index].index(item)
        return self.values[index][internal_index]

    def get(self, key):
        return self.__getitem__(key)

    def remove(self, key):
        index = self.get_index(key)
        if key not in self.keys[index]:
            raise KeyError(key)
        internal_index = self.keys[index].index(key)
        self.keys[index].pop(internal_index)
        self.values[index].pop(internal_index)
        self.count -= 1

    def __contains__(self, item):
        index = self.get_index(item)
        return True if item in self.keys[index] else False

    def __len__(self):
        return self.count


table = HashTable()

table["name"] = "Peter"
table["age"] = 25
table["age"] = 26

print(table)
print(table.get("name"))
print(table["age"])
print(len(table))
print("age" in table)
table.remove("age")
print("age" in table)
print(len(table))
