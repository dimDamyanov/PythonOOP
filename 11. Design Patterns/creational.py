def singleton(cls):
    instance = None

    def wrapper(*args, **kwargs):
        nonlocal instance
        if not instance:
            instance = cls(*args, **kwargs)
        return instance

    return wrapper


@singleton
class JsonParser:
    @staticmethod
    def parse(obj):
        return f'json: {str(obj)}'


parser = JsonParser()
print(id(JsonParser()))
print(id(JsonParser()))