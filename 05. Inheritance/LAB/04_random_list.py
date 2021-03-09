import random


class RandomList(list):
    def get_random_element(self):
        # random_index = random.randint(0, len(self) - 1)
        # return self.pop(random_index)
        random_element = random.choice(self)
        self.remove(random_element)
        return random_element


random_list = RandomList([1, 2, 3, 4, 5, 6, 7, 8, 9])
while random_list:
    print(random_list.get_random_element())
