import functools


class uppercase:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs).upper()


def repeat(count):
    class decorator:
        def __init__(self, func):
            self.func = func

        def __call__(self, *args, **kwargs):
            for _ in range(count):
                self.func(*args, **kwargs)

    return decorator


@repeat(17)
def print_something():
    print('Hello')


# print(get_message())
# print_something()


class cache:
    def __init__(self, func):
        self.func = func
        self.internal_cache = {}

    def __call__(self, *args, **kwargs):
        cache_key = args + tuple(kwargs.values())
        if cache_key not in self.internal_cache:
            self.internal_cache[cache_key] = self(*args, **kwargs)
        return self.internal_cache[cache_key]


class logger:
    log_file_path = './log.txt'

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        args_str = [str(e) for e in args]
        kwargs_str = [f'{key}={value}' for key, value in kwargs.items()]
        arguments_str = []
        arguments_str.extend(args_str)
        arguments_str.extend(kwargs_str)
        result = self.func(*args, **kwargs)
        with open(self.log_file_path, 'a') as file:
            file.write(f'{self.func.__name__}({", ".join(arguments_str)}) returned {result}\n')
        return result


@uppercase
@logger
def get_message():
    return 'Hi dadasdsd'


get_message()