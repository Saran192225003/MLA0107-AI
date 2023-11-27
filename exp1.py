import heapq

class PuzzleNode:
    def __init__(self, state, parent=None, move=None, cost=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

def heuristic(state, goal_state):
    # Manhattan distance heuristic
    total_distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                goal_row, goal_col = divmod(goal_state.index(state[i][j]), 3)
                total_distance += abs(i - goal_row) + abs(j - goal_col)
    return total_distance

def get_neighbors(state):
    neighbors = []
    empty_row, empty_col = None, None
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                empty_row, empty_col = i, j
                break

    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Possible moves: right, left, down, up

    for move in moves:
        new_row, new_col = empty_row + move[0], empty_col + move[1]
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = [row[:] for row in state]
            new_state[empty_row][empty_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_row][empty_col]
            neighbors.append(new_state)

    return neighbors

def solve_puzzle(initial_state, goal_state):
    initial_node = PuzzleNode(initial_state)
    goal_node = PuzzleNode(goal_state)

    open_set = [initial_node]
    closed_set = set()

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.state == goal_node.state:
            path = []
            while current_node.parent:
                path.append(current_node.move)
                current_node = current_node.parent
            path.reverse()
            return path

        closed_set.add(tuple(map(tuple, current_node.state)))

        for neighbor_state in get_neighbors(current_node.state):
            if tuple(map(tuple, neighbor_state)) not in closed_set:
                neighbor_node = PuzzleNode(neighbor_state, current_node, neighbor_state[current_node.state.index(0)].index(0), current_node.cost + 1 + heuristic(neighbor_state, goal_state))
                heapq.heappush(open_set, neighbor_node)

    return None

def print_puzzle(state):
    for row in state:
        print(row)

if __name__ == "__main__":
    initial_state = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 5, 8]
    ]

    goal_state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    print("Initial State:")
    print_puzzle(initial_state)

    print("\nGoal State:")
    print_puzzle(goal_state)

    solution = solve_puzzle(initial_state, goal_state)

    if solution:
        print("\nSolution:")
        for move in solution:
            print(move)
    else:
        print("\nNo solution found.")
