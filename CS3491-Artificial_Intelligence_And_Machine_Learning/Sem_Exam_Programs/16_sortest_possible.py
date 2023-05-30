import heapq

class Node:
    def __init__(self, state, parent, cost, heuristic):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def astar(start, goal, graph, cost_func, heuristic_func):
    heap = []
    heapq.heappush(heap, (0, Node(start, None, 0, 0)))
    visited = set()

    while heap:
        (cost, current) = heapq.heappop(heap)

        if current.state == goal:
            path = []
            while current is not None:
                path.append(current.state)
                current = current.parent
            # Return reversed path
            return path[::-1]

        if current.state in visited:
            continue

        visited.add(current.state)

        for state, cost in graph[current.state].items():
            if state not in visited:
                heuristic = heuristic_func(state, goal)
                heapq.heappush(heap, (cost, Node(state, current, current.cost + cost, heuristic)))

    return None  # No path found

# Example cost function
def cost_func(state1, state2):
    # Calculate the cost between two states
    # You can modify this function based on your problem
    return graph[state1][state2]

# Example heuristic function (Euclidean distance)
def heuristic_func(state, goal):
    # Calculate the heuristic value for a state
    # You can modify this function based on your problem
    return 0

graph = {
    'A': {'B': 1, 'D': 3},
    'B': {'A': 1, 'C': 2, 'D': 4},
    'C': {'B': 2, 'D': 5, 'E': 2},
    'D': {'A': 3, 'B': 4, 'C': 5, 'E': 3},
    'E': {'C': 2, 'D': 3}
}

start = 'A'
goal = 'E'
result = astar(start, goal, graph, cost_func, heuristic_func)

if result:
    print("Shortest path:", result)
else:
    print("No path found.")
