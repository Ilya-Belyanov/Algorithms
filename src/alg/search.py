def binarySearch(massive, item):
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


def minSearch(massive):
    minItem = massive[0]
    idMin = 0
    for i in range(1, len(massive)):
        if massive[i] < minItem:
            minItem = massive[i]
            idMin = i
    return idMin


def maxSearch(massive):
    maxItem = massive[0]
    idMax = 0
    for i in range(1, len(massive)):
        if massive[i] > maxItem:
            maxItem = massive[i]
            idMax = i
    return idMax
