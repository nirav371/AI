def bfs(graph, node,goal):
    visited = []
    queue = []
    traverslLst = []

    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        traverslLst.append(m)
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
        if traverslLst[-1]==goal:
            return traverslLst
        


graph = {
    "5": ['3', '7'],
    "3": ['2', '4'],
    "7": ['8'],
    "2": [],
    "4": ['8'],
    "8": [],
}
node = input("Input starting node : ")
goal = input("Input Ending node : ")

traversalPath = bfs(graph, node,goal)

print("Traversal path is :-", traversalPath)
