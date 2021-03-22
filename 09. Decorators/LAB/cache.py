import functools


def cache(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        cache_key = args + tuple(kwargs.values())
        if cache_key not in wrapper.internal_cache:
            wrapper.internal_cache[cache_key] = func(*args, **kwargs)
        return wrapper.internal_cache[cache_key]

    wrapper.internal_cache = {}
    return wrapper


@cache
def fibonacci(n):
    print(f'Calculating F({n})')
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)


@cache
def test(n):
    print(f'T({n})')
    return 5


print(fibonacci(111))
print(fibonacci(10))
print(test(100))
print(test(100))
print(test(101))
print(fibonacci(10))
print(test.internal_cache)
print(fibonacci.internal_cache)
