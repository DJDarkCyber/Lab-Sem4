graph = {
    '5' : ['3','7'],
    '3' : ['2', '4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
}

visited = []
queue = []

def bfs(visited, queue, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end=" ")

        for neighour in graph[m]:
            if neighour not in visited:
                visited.append(neighour)
                queue.append(neighour)


print("The following is the breadth first search ")
bfs(visited, queue, '5')
