def binary_search(massive, item):
    """ In an order of increasing or descending"""
    low = 0
    high = len(massive) - 1
    direct = 1 if massive[high] > massive[low] else -1
    while low <= high:
        mid = int((low + high) / 2)
        guess = massive[mid]
        if (guess * direct) > (item * direct):
            high = mid - 1
        elif (guess * direct) < (item * direct):
            low = mid + 1
        else:
            return mid


def min_search(massive):
    min_item = massive[0]
    id_min = 0
    for i in range(1, len(massive)):
        if massive[i] < min_item:
            min_item = massive[i]
            id_min = i
    return id_min


def max_search(massive):
    max_item = massive[0]
    id_max = 0
    for i in range(1, len(massive)):
        if massive[i] > max_item:
            max_item = massive[i]
            id_max = i
    return id_max
