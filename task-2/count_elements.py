from collections import defaultdict

list_version = [
    ['665587', 2],
    ['669532', 1],
    ['669537', 2],
    ['669532', 1],
    ['665587', 1],
]


def count_occurencies(lst: list[list]) -> list[list]:
    '''
    Counts the occurrences of pairs in a list and
    returns the result in the specified format.
    '''
    counts = defaultdict(int)
    for item in list_version:
        counts[(item[0], item[1])] += 1
    result = []
    for key, value in counts.items():
        result.append([key[0], key[1], value])

    return result


print(count_occurencies(list_version))
# [['665587', 2, 1], ['669532', 1, 2], ['669537', 2, 1], ['665587', 1, 1]]
