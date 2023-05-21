def transitive_closure(graph):
    # The number of vertices
    n = len(graph)
    closure = [[0 for j in range(n)] for i in range(n)]

    # Initialize the closure matrix with the graph values
    for i in range(n):
        for j in range(n):
            closure[i][j] = graph[i][j]

    # Calculate transitive closure
    for k in range(n):
        for i in range(n):
            for j in range(n):
                closure[i][j] = closure[i][j] or (closure[i][k] and closure[k][j])

    return closure

# Input
graph = [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0]
]
closure = transitive_closure(graph)
print(closure)
