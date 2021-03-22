def vowel_filter(function):
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}

    def wrapper():
        result = function()
        return [ch for ch in result if ch.casefold() in vowels]
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
