from search import minSearch, maxSearch


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


def fastSort(massive, sort=True):
    """ sort = True -> in an order of increasing, otherwise in an order of descending"""
    if len(massive) < 2:
        return massive
    else:
        direct = 1 if sort else -1
        first = massive[0]
        left = [i for i in massive[1:] if (i * direct) <= (first * direct)]
        right = [i for i in massive[1:] if (i * direct) > (first * direct)]

        return fastSort(left, sort) + [first] + fastSort(right, sort)