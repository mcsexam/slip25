from collections import deque

def display(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

def get_moves(state):
    moves = []
    index = state.index(0) 
    row, col = index // 3, index % 3
    directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
    
    for move, (r, c) in directions.items():
        new_row, new_col = row + r, col + c
        if 0 <= new_row < 3 and 0 <= new_col < 3: 
            new_index = new_row * 3 + new_col
            new_state = list(state)
            new_state[index], new_state[new_index] = new_state[new_index], new_state[index]  
            moves.append(tuple(new_state))
    return moves

def solve_8_puzzle(start, goal):
    visited = set()  
    queue = deque([(start, [])]) 
    
    while queue:
        state, path = queue.popleft()
        
        if state == goal:
            return path + [state]
        
        visited.add(state)
        
        for move in get_moves(state):
            if move not in visited:
                queue.append((move, path + [state]))
    
    return None 

start = (1, 2, 3, 4, 0, 5, 6, 7, 8)
goal = (1, 2, 3, 4, 5, 0, 6, 7, 8)

solution = solve_8_puzzle(start, goal)

print("Steps to solve 8-Puzzle:\n")
if solution:
    for step in solution:
        display(step)
else:
    print("No solution found.")
