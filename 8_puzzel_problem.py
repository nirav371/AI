from collections import deque

def bfs(start, goal):
    queue = deque([(start, [start])])
    while queue:
        (state, path) = queue.popleft()
        if state == goal:
            return path
        for neighbor in get_neighbors(state):
            queue.append((neighbor, path + [neighbor]))

def get_neighbors(state):
    zero_index = state.index(0)
    row, col = divmod(zero_index, a)
    neighbors = []
    if row > 0:
        up_state = state[:]
        up_state[zero_index], up_state[zero_index - a] = up_state[zero_index - a], up_state[zero_index]
        neighbors.append(up_state)
    if row < (a-1):
        down_state = state[:]
        down_state[zero_index], down_state[zero_index + a] = down_state[zero_index + a], down_state[zero_index]
        neighbors.append(down_state)
    if col > 0:
        left_state = state[:]
        left_state[zero_index], left_state[zero_index - 1] = left_state[zero_index - 1], left_state[zero_index]
        neighbors.append(left_state)
    if col < (a-1):
        right_state = state[:]
        right_state[zero_index], right_state[zero_index + 1] = right_state[zero_index + 1], right_state[zero_index]
        neighbors.append(right_state)
    return neighbors

a = 3
start = [1, 2, 3, 4, 5, 6, 0, 7, 8]
goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
path = bfs(start, goal)
for state in path:
    print(state[0:3])
    print(state[3:6])
    print(state[6:9])
    print(state[0:])
    print()
