def debug(func):
    """Print func name with args, kwargs and result"""

    def wrapper(*args, **kwargs):
        args_str = [str(e) for e in args]
        kwargs_str = [f'{key}={value}' for key, value in kwargs.items()]
        arguments_str = []
        arguments_str.extend(args_str)
        arguments_str.extend(kwargs_str)
        result = func(*args, **kwargs)
        print(f'{func.__name__}({", ".join(arguments_str)}) returned {result}')
        return result

    return wrapper


@debug
def get_hello(name):
    return f'Hello, {name}'


get_hello('Daniel')
