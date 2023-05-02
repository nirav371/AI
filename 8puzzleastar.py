import copy
startstate =[[1, "_", 2], [6, 7, 4], [8, 5, 3]]
goalstate = [[1, 2, 3], [4, 5, 6], [7, 8, '_']]

visited = []
queue = [startstate]

def getNext(node):
    nextStates = []
    for row in range(0, len(node)):
        for col in range(0, len(node[row])):
            if(node[row][col]=='_'):
                if(row==0 or row==1):
                    a = copy.deepcopy(node)
                    a[row][col], a[row+1][col] = a[row+1][col], a[row][col]
                    nextStates.append(a)

                if(row==1 or row==2):
                    a = copy.deepcopy(node)
                    a[row][col], a[row-1][col] = a[row-1][col], a[row][col]
                    nextStates.append(a)
                
                if(col==0 or col==1):
                    a = copy.deepcopy(node)
                    a[row][col], a[row][col+1] = a[row][col+1], a[row][col]
                    nextStates.append(a)

                if(col==1 or col==2):
                    a = copy.deepcopy(node)
                    a[row][col], a[row][col-1] = a[row][col-1], a[row][col]
                    nextStates.append(a)
    
    return nextStates

def minCost(states):
    costs={}
    for state in states:
        if state not in visited:
            cost = 0
            for row in range(0, len(state)):
                for col in range(0, len(state[row])):
                    if(state[row][col] != goalstate[row][col]):
                        cost = cost + 1
            costs[cost]=state
    lst = list(costs.items())
    lst.sort()
    costs = dict(lst)
    return list(costs.values())

while(len(queue)>0):
    node = queue.pop(0)
    if node not in visited:
        print(node, end = " ")
        if(node == goalstate):
            break
        print('\n\nnext state\n')
        visited.append(node)
        queue[:0]= minCost(getNext(node))