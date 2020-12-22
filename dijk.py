def dijkSearch(graph, userstart=None, userfinish=None):
    verified = []
    start = __checkStart(graph, userstart)
    costs = __countCosts(graph, start)
    parents = __countParents(graph, start)
    node = __lowerCost(costs, verified)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for key in neighbors.keys():
            newCost = cost + neighbors[key]
            if costs[key] > newCost:
                costs[key] = newCost
                parents[key] = node
        verified.append(node)
        node = __lowerCost(costs, verified)
    return __result(parents, costs, graph, start, userfinish)


def __result(parents, costs, graph, start, finish):
    __path = __countWay(parents, graph, start, finish)
    __inversePath = [__path[len(__path) - i] for i in range(1, len(__path) + 1)]
    __cost = costs[__path[0]]
    __inversePath.append(__cost)
    return __inversePath


def __countWay(parents, graph, start, finish):
    path = []
    fin = __checkFinal(graph, finish)
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


def __checkFinal(graph, finish):
    if finish:
        return finish
    for __node in graph:
        if not graph[__node].keys():
            return __node
    return None


def __checkStart(graph, start):
    if start:
        return start
    __nodeKey = set()
    for __key in graph.keys():
        __nodeKey |= set(graph[__key].keys())
    for __start in set(graph.keys()) - __nodeKey:
        return __start
    return None


def __countCosts(graph, __start):
    return {i: graph[__start][i] if i in graph[__start].keys() else float('inf') if i != __start else 0 for i in
            graph.keys()}


def __countParents(graph, __start):
    return {i: __start if i in graph[__start].keys() else None for i in graph.keys()}


def __lowerCost(costs, verified):
    lowCost = float('inf')
    lowCostNode = None
    for node in costs:
        cost = costs[node]
        if cost < lowCost and node not in verified:
            lowCost = cost
            lowCostNode = node
    return lowCostNode
