import functools
from time import time


def measure_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'{func.__name__} executed in {end - start} ms')
        return result

    return wrapper


@measure_time
def big_loop():
    x = 0
    for _ in range(10000000):
        x += 1
    return x


big_loop()
