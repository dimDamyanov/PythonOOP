def read_next(*args):
    l = [el for x in args for el in list(x)]
    index = 0
    while index < len(l):
        yield l[index]
        index += 1


for item in read_next('string', (2,), {'d': 1, 'i': 2, 'c': 3, 't': 4}):
    print(item, end='')
