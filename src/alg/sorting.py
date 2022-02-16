from search import minSearch, maxSearch
from src.alg.listalg import swap


def selectSort(massive, sort=True):
    """ sort = True -> in an order of increasing, otherwise in an order of descending"""
    newMassive = []
    functions = (minSearch, maxSearch)
    if sort:
        idFunction = 0
    else:
        idFunction = 1

    for i in range(len(massive)):
        idMin = functions[idFunction](massive)
        newMassive.append(massive.pop(idMin))

    return newMassive


def compare(a, b):
    return a > b


def bubbleSort(massive, sort=True):
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


def fastSort(massive, sort=True):
    """ sort = True -> in an order of increasing, otherwise in an order of descending"""
    if len(massive) < 2:
        return massive

    left, right = list(), list()
    for item in massive[1:]:
        if (item <= massive[0]) is sort:
            left.append(item)
        else:
            right.append(item)
    return fastSort(left, sort) + [massive[0]] + fastSort(right, sort)
