def process_rule(graph, line):
    """
    Processes a single rule from input and updates the graph
    """
    line = line.split()

    # check if the bag is allowed to hold other bags:
    if len(line) == 7:
        return graph
    else:
        large = line[0] + "_" + line[1]
        for i in range(int(len(line) / 4 - 1)):
            item = line[4 * i + 5] + "_" + line[4 * i + 6]

            # add key of not existent
            if item not in graph.keys():
                graph[item] = []

            # update values
            graph[item].append(large)

    # Return updated rule graph
    return graph


def process_rule_part2(graph, line):
    """
    Processes a single rule from input and updates the graph
    """
    line = line.split()

    # Add element for the large bag
    large = line[0] + "_" + line[1]
    if large not in graph.keys():
        graph[large] = {}

    if len(line) == 7:
        return graph
    else:
        for i in range(int(len(line) / 4 - 1)):
            num = int(line[4 * i + 4])
            item = line[4 * i + 5] + "_" + line[4 * i + 6]

            # add key of not existent
            graph[large][item] = num

    # Return updated rule graph
    return graph


def total_bags_from_color(graph, vertex):
    """
    Calculates the total number of bags needed from a color
    """
    if len(graph[vertex]) == 0:
        return 1
    else:
        total = 1
        for color in graph[vertex].keys():
            total += graph[vertex][color] * total_bags_from_color(graph, color)

    # Return final list
    return total


def accessible_vertices(graph, vertex):
    """
    Find all vertices accesible from the given vertex
    """
    visited = []
    to_visit = graph[vertex].copy()
    while len(to_visit) > 0:
        v = to_visit.pop()
        visited.append(v)
        # add all vertices accessible from v
        if v in graph.keys():
            for acc in graph[v]:
                if acc not in to_visit and acc not in visited:
                    to_visit.append(acc)

    # Return final list
    return visited
