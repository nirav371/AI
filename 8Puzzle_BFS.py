from collections import deque

def print_puzzle(puzzle):
    """
    Prints the puzzle matrix.
    """
    for i in range(3):
        print(puzzle[i*3:i*3+3])
    print()

def is_solvable(puzzle):
    """
    Returns True if the puzzle is solvable, False otherwise.
    """
    inversion_count = 0
    for i in range(len(puzzle)):
        for j in range(i + 1, len(puzzle)):
            if puzzle[i] != 0 and puzzle[j] != 0 and puzzle[i] > puzzle[j]:
                inversion_count += 1
    return inversion_count % 2 == 0

def bfs(start, end):
    """
    Returns a list of moves to go from the start state to the end state using BFS.
    """
    if not is_solvable(start) or not is_solvable(end):
        return None
    queue = deque([(start, [])])
    visited = set([tuple(start)])
    while queue:
        puzzle, moves = queue.popleft()
        if puzzle == end:
            return moves
        zero_index = puzzle.index(0)
        row, col = zero_index // 3, zero_index % 3
        # row, col: UP, DOWN, LEFT, RIGHT
        for r, c in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
            if 0 <= r < 3 and 0 <= c < 3:
                new_puzzle = puzzle[:]
                new_puzzle[zero_index], new_puzzle[r * 3 + c] = new_puzzle[r * 3 + c], new_puzzle[zero_index]
                if tuple(new_puzzle) not in visited:
                    visited.add(tuple(new_puzzle))
                    queue.append((new_puzzle, moves + [(r, c)]))
    return None

# Example usage
start = [1, 2, 3, 4, 0, 5, 6, 7, 8] #Solvable start state since number of inversions is even
# start = [1, 3, 2, 5, 6, 0, 7, 8, 4] #UnSolvable Start State since number of inversions is odd
end = [1, 2, 3, 4, 5, 6, 7, 8, 0]
moves = bfs(start, end)
if moves is None:
    print("No solution found.")
else:
    puzzle = start
    print_puzzle(puzzle)
    for r, c in moves:
        zero_index = puzzle.index(0)
        puzzle[zero_index], puzzle[r * 3 + c] = puzzle[r * 3 + c], puzzle[zero_index]
        print_puzzle(puzzle)
    print("Goal state reached!")
