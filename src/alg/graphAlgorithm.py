def backpackAlg(graph: dict, length: int):
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


def setOptimization(need: set, has: dict):
    """Count coverage cost optimization"""
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


def rGraphSearch(queue, graph: dict, checkFunction, verified: list = []):
    """Меняет queue!!!"""
    if not queue:
        return None
    else:
        person = queue.popleft()
        if person not in verified:
            if checkFunction(person):
                return person
            else:
                queue += graph[person]
                verified += person
        return rGraphSearch(queue, graph, verified)


def lGraphSearch(queue, graph: dict, checkFunction):
    verified = []
    que = queue.copy()

    while que:
        person = que.popleft()
        if person not in verified:
            if checkFunction(person):
                return person
            else:
                que += graph[person]
                verified.append(person)
