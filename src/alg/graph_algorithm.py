def backpack(graph: dict, length: int):
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

        inverse_costs, inverse_name = costs, name
        costs = [list(inverse_costs[j]) for j in range(-1, 1)]
        name = [list(inverse_name[j]) for j in range(-1, 1)]
    return costs[0][length], name[0][length]


def set_optimization(need: set, has: dict):
    """Count coverage cost optimization"""
    final = set()
    while need:
        best = None
        best_covered = set()
        for name, item in has.items():
            covered = need & item
            if len(covered) > len(best_covered):
                best = name
                best_covered = covered
        need -= best_covered
        final.add(best)
    return final


def graph_search_r(queue, graph: dict, check_function, verified=None):
    """Меняет queue!!!"""
    if verified is None:
        verified = []
    if not queue:
        return None
    person = queue.popleft()
    if person not in verified:
        if check_function(person):
            return person
        queue += graph[person]
        verified += person
    return graph_search_r(queue, graph, verified)


def graph_search_l(queue, graph: dict, check_function):
    verified = []
    que = queue.copy()

    while que:
        person = que.popleft()
        if person in verified:
            continue
        if check_function(person):
            return person
        que += graph[person]
        verified.append(person)
