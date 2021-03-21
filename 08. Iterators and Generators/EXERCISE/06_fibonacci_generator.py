def fibonacci():
    x = 0
    y = 1
    while True:
        yield x
        z = x + y
        x = y
        y = z


generator = fibonacci()
for i in range(5):
    print(next(generator))
