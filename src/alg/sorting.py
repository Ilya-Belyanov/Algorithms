from search import min_search, max_search
from src.alg.listalg import swap


def select_sort(massive, sort=True):
    """ sort = True -> in an order of increasing, otherwise in an order of descending"""
    new_massive = []
    functions = (min_search, max_search)
    if sort:
        id_function = 0
    else:
        id_function = 1

    for _ in range(len(massive)):
        id_min = functions[id_function](massive)
        new_massive.append(massive.pop(id_min))
    return new_massive


def compare(first, second):
    return first > second


def bubble_sort(massive, sort=True):
    """ sort = True -> in an order of increasing, otherwise in an order of descending"""
    for i in range(len(massive) - 1):
        is_swap = False
        for j in range(len(massive) - i - 1):
            if compare(massive[j], massive[j + 1]) is sort:
                massive = swap(massive, j, j + 1)
                is_swap = True
        if not is_swap:
            break
    return massive


def fast_sort(massive, sort=True):
    """ sort = True -> in an order of increasing, otherwise in an order of descending"""
    if len(massive) < 2:
        return massive

    left, right = list(), list()
    for item in massive[1:]:
        if (item <= massive[0]) is sort:
            left.append(item)
        else:
            right.append(item)
    return fast_sort(left, sort) + [massive[0]] + fast_sort(right, sort)
