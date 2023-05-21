INF = 99999999

def floyd(graph):
    # The number of vertices
    n = len(graph)
    INF = float('inf')
    dist = [[INF] * n for _ in range(n)]

    # Initialize the distance matrix with the graph values
    for i in range(n):
        for j in range(n):
            dist[i][j] = graph[i][j]

    # Calculate shortest path for all vertices
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

# Input
graph = [[0, 3, INF, 5], [2, 0, INF, 4], [INF, 1, 0, INF], [INF, INF, 2, 0]]
result = floyd(graph)
print(result)
