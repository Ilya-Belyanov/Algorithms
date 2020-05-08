""" Reductions using in the names of algorithms:
        r - recursion
        l - loop
        s - selection
        f - fast
"""


def decorResult(result):
    def wrapper(cls, parents, costs, graph, start, finish):
        res = result(cls, parents, costs, graph, start, finish)
        text = 'Short path is '
        for i in range(len(res) - 1):
            try:
                text += res[i] + ' -> '
            except TypeError:
                return 'Incorrect values'
        text += ' with cost = ' + str(res[len(res) - 1])
        return text

    return wrapper


class Algorithms:

    @classmethod
    def dijkSearch(cls, graph, userstart=None, userfinish=None):
        verified = []
        start = cls.__checkStart(graph, userstart)
        costs = cls.__countCosts(graph, start)
        parents = cls.__countParents(graph, start)
        node = cls.__lowerCost(costs, verified)
        while node is not None:
            cost = costs[node]
            neighbors = graph[node]
            for key in neighbors.keys():
                newCost = cost + neighbors[key]
                if costs[key] > newCost:
                    costs[key] = newCost
                    parents[key] = node
            verified.append(node)
            node = cls.__lowerCost(costs, verified)
        return cls.__result(parents, costs, graph, start, userfinish)

    @classmethod
    #@decorResult
    def __result(cls, parents, costs, graph, start, finish):
        __path = cls.__countWay(parents, graph, start, finish)
        __inversePath = [__path[len(__path) - i] for i in range(1, len(__path) + 1)]
        __cost = costs[__path[0]]
        __inversePath.append(__cost)
        return __inversePath

    @classmethod
    def __countWay(cls, parents, graph, start, finish):
        path = []
        fin = cls.__checkFinal(graph, finish)
        path.append(fin)
        for i in range(len(parents.keys())):
            if path[len(path) - 1] == start:
                break
            try:
                path.append(parents[path[len(path) - 1]])
            except KeyError:
                path.append(None)
                break
        return path

    @staticmethod
    def __checkFinal(graph, finish):
        if finish:
            return finish
        for __node in graph:
            if not graph[__node].keys():
                return __node
        return None

    @staticmethod
    def __checkStart(graph, start):
        if start:
            return start
        __nodeKey = set()
        for __key in graph.keys():
            __nodeKey |= set(graph[__key].keys())
        for __start in set(graph.keys()) - __nodeKey:
            return __start
        return None

    @classmethod
    def __countCosts(cls, graph, __start):
        return {i: graph[__start][i] if i in graph[__start].keys() else float('inf') if i != __start else 0 for i in
                graph.keys()}

    @classmethod
    def __countParents(cls, graph, __start):
        return {i: __start if i in graph[__start].keys() else None for i in graph.keys()}

    @staticmethod
    def __lowerCost(costs, verified):
        lowCost = float('inf')
        lowCostNode = None
        for node in costs:
            cost = costs[node]
            if cost < lowCost and node not in verified:
                lowCost = cost
                lowCostNode = node
        return lowCostNode

    @classmethod
    def backpackAlg(cls, graph, length):
        costs = [[0 for i in range(length + 1)] for j in range(2)]
        name = [['' for i in range(length + 1)] for j in range(2)]
        for key in graph.keys():
            weight, cost = graph[key][0], graph[key][1]
            for i in range(1, length + 1):
                if weight > i:
                    costs[1][i] = costs[0][i]
                    name[1][i] = name[0][i]
                elif cost + costs[0][i - weight] > costs[0][i]:
                    costs[1][i] = cost + costs[0][i - weight]
                    name[1][i] = key + ' ' + name[0][i - weight]
                else:
                    costs[1][i] = costs[0][i]
                    name[1][i] = name[0][i]

            inverseCosts, inverseName = costs, name
            costs = [[i for i in inverseCosts[j]] for j in range(-1, 1)]
            name = [[i for i in inverseName[j]] for j in range(-1, 1)]
        return costs[0][length], name[0][length]

    @classmethod
    def setOptimization(cls, need, has):
        """Count coverage cost optimization:need - set(), has - dict()"""
        final = set()
        while need:
            best = None
            bestCovered = set()
            for name, item in has.items():
                covered = need & item
                if len(covered) > len(bestCovered):
                    best = name
                    bestCovered = covered
            need -= bestCovered
            final.add(best)
        return final

    @classmethod
    def rGraphSearch(cls, queue, graph, letter, verified=()):
        """Меняет queue!!!"""
        if not queue:
            return None
        else:
            person = queue.popleft()
            if person not in verified:
                if cls.__checkPerson(person, letter):
                    return person
                else:
                    queue += graph[person]
                    verified = list(verified)
                    verified.append(person)
                    verified = tuple(verified)
            return cls.rGraphSearch(queue, graph, letter, verified)

    @classmethod
    def lGraphSearch(cls, queue, graph, letter):
        verified = []
        que = queue.copy()
        while que:
            person = que.popleft()
            if person not in verified:
                if cls.__checkPerson(person, letter):
                    return person
                else:
                    que += graph[person]
                    verified.append(person)
        return None

    @staticmethod
    def __checkPerson(person, letter):
        return person[-1] == letter

    @classmethod
    def binarySearch(cls, massive, item):
        """ In an order of increasing or descending"""
        low = 0
        high = len(massive) - 1
        direct = cls.__checkSort(massive[high] > massive[low])
        while low <= high:
            mid = int((low + high) / 2)
            guess = massive[mid]
            if (guess * direct) > (item * direct):
                high = mid - 1
            elif (guess * direct) < (item * direct):
                low = mid + 1
            else:
                return mid
        return None

    @classmethod
    def minSearch(cls, massive):
        minItem = massive[0]
        idMin = 0
        for i in range(1, len(massive)):
            if massive[i] < minItem:
                minItem = massive[i]
                idMin = i

        return idMin

    @classmethod
    def maxSearch(cls, massive):
        maxItem = massive[0]
        idMax = 0
        for i in range(1, len(massive)):
            if massive[i] > maxItem:
                maxItem = massive[i]
                idMax = i

        return idMax

    @classmethod
    def sSort(cls, massive, sort=True):
        """ sort = True -> in an order of increasing, otherwise in an order of descending"""
        newMassive = []
        functions = (cls.minSearch, cls.maxSearch)
        if sort:
            idFunction = 0
        else:
            idFunction = 1

        for i in range(len(massive)):
            idMin = functions[idFunction](massive)
            newMassive.append(massive.pop(idMin))

        return newMassive

    @classmethod
    def fSort(cls, massive, sort=True):
        """ sort = True -> in an order of increasing, otherwise in an order of descending"""
        if len(massive) < 2:
            return massive
        else:
            direct = cls.__checkSort(sort)
            first = massive[0]
            left = [i for i in massive[1:] if (i * direct) <= (first * direct)]
            right = [i for i in massive[1:] if (i * direct) > (first * direct)]

            return cls.fSort(left, sort) + [first] + cls.fSort(right, sort)

    @staticmethod
    def __checkSort(sort):
        if sort:
            return 1
        else:
            return -1

    @classmethod
    def checkRepeat(cls, table, name):
        if table.get(name) is not None:
            return True
        else:
            return False

    @classmethod
    def rFactorial(cls, x):
        if x == 0:
            return 1
        else:
            return x * cls.rFactorial(x - 1)

    @classmethod
    def lFactorial(cls, x):
        count = 1
        for i in range(1, x + 1):
            count *= i
        return count

    @classmethod
    def rSum(cls, massive):
        if not massive:
            return 0
        else:
            return massive[0] + cls.rSum(massive[1:])

    @classmethod
    def lSum(cls, massive):
        count = 0
        for i in massive:
            count += i
        return count
