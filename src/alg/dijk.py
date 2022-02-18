def dijk_search(graph, user_start=None, user_finish=None):
    verified = []
    start = _check_start(graph, user_start)
    costs = _count_costs(graph, start)
    parents = _count_parents(graph, start)
    node = _lower_cost(costs, verified)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for key in neighbors.keys():
            new_cost = cost + neighbors[key]
            if costs[key] > new_cost:
                costs[key] = new_cost
                parents[key] = node
        verified.append(node)
        node = _lower_cost(costs, verified)
    return _result(parents, costs, graph, start, user_finish)


def _result(parents, costs, graph, start, finish):
    path = _count_way(parents, graph, start, finish)
    inverse_path = [path[len(path) - i] for i in range(1, len(path) + 1)]
    cost = costs[path[0]]
    inverse_path.append(cost)
    return inverse_path


def _count_way(parents, graph, start, finish):
    path = []
    fin = _check_final(graph, finish)
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


def _check_final(graph, finish):
    if finish:
        return finish
    for __node in graph:
        if not graph[__node].keys():
            return __node
    return None


def _check_start(graph, start):
    if start:
        return start
    node_key = set()
    for key in graph.keys():
        node_key |= set(graph[key].keys())
    for start in set(graph.keys()) - node_key:
        return start
    return None


def _count_costs(graph, start):
    return {i: graph[start][i] if i in graph[start].keys() else float('inf') if i != start else 0 for i in
            graph.keys()}


def _count_parents(graph, start):
    return {i: start if i in graph[start].keys() else None for i in graph.keys()}


def _lower_cost(costs, verified):
    low_cost = float('inf')
    low_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < low_cost and node not in verified:
            low_cost = cost
            low_cost_node = node
    return low_cost_node
