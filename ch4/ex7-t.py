def build_order(projects, dependencies):
    adj_list = {}
    in_deg = {}
    no_edges = []
    result = []

    for project in projects:
        adj_list[project] = []
        in_deg[project] = 0

    for first, second in dependencies:
        adj_list[first].append(second)
        in_deg[second] += 1

    for project in in_deg:
        if in_deg[project] == 0:
            no_edges.append(project)

    while no_edges:
        node = no_edges.pop()

        for project in adj_list[node]:
            in_deg[project] -= 1
            if in_deg[project] == 0:
                no_edges.append(project)

        result.append(node)

    if len(result) == len(projects):
        return result
    else:
        return None
