def dfs(visited,graph,node):
    if(node in visited):
        return
    else:
        visited.append(node)
        temp_node= graph[node]

        if(len(temp_node)==0):
            print(node+" ",end="")
            return
        else:
            for i in range(len(temp_node)):
                dfs(visited,graph,temp_node[i])
            print(node+" " , end="")
            return 


graph={
    'A':['B','C'],
    'B':['D','A'],
    'C':[],
    'D':['E','F'],
    'E':['G'],
    'F':[],
    'G':['H'],
    'H':[]
}

node_len = len(graph)
n_node = input("Enter the starting node:")
visited=[]
print("Stack Flow:")
dfs(visited,graph,n_node)
print(visited)