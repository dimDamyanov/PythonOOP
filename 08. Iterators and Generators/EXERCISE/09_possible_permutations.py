from itertools import permutations


def possible_permutations(elements):
    for permutation in permutations(elements):
        yield list(permutation)


[print(n) for n in possible_permutations([1, 2, 3])]