graph = {
'A':['B','C'],
'B':['D'],
'C':['E','F'],
'D':['G'],
'E':[],
'F':['H'],
'G':['I'],
'H':[],
'I':[]
}
queue = []
def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node) 
    while queue:
        m = queue.pop(0)
        print (m, end = " ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
        if m==goal:
            break
goal = input("Enter Goal node: ").upper()
bfs([], graph, 'A')