def find_path(graph, start, end, path=[]):
    path = path + [start]

    if start == end:
        return path

    for node in graph[start]:
        if node not in path:
            newp = find_path(graph, node, end, path)
            if newp:
                return newp


# ============== #
# The main code  #
# ============== #
# This code finds a path (not the shortest one) in a graph.

# E.G.
# Let's define a graph as a dictionary:
graph = {
    'A': ['B', 'F'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['C', 'E'],
    'E': ['D', 'F'],
    'F': ['E', 'A']}

path = find_path(graph, 'B', 'C')
print(path)
