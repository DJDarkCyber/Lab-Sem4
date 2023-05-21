from sys import maxsize
from itertools import permutations

V = 4

def travellingSalesmanProblem(graph, s):
    # store all vertices apart from the source vertex
    vertices = []
    for i in range(V):
        if i != s:
            vertices.append(i)

    # store minimum weight Hamiltonian Cycle
    min_path = maxsize
    next_permutations = permutations(vertices)

    for perm in next_permutations:
        # store current path weight (cost)
        current_path_weight = 0
        k = s

        for j in perm:
            current_path_weight += graph[k][j]
            k = j

        current_path_weight += graph[k][s]
        # update minimum path
        min_path = min(min_path, current_path_weight)

    return min_path

# Driver Code
if __name__ == "__main__":
    # matrix representation of the graph
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    s = 0  # starting vertex
    print(travellingSalesmanProblem(graph, s))
