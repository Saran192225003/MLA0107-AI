import heapq

class AStar:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

    def heuristic(self, current, goal):
        return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

    def is_valid_move(self, position):
        row, col = position
        return 0 <= row < self.rows and 0 <= col < self.cols and self.grid[row][col] != 1

    def generate_neighbors(self, current):
        neighbors = []
        row, col = current

        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)] 

        for move in moves:
            new_pos = (row + move[0], col + move[1])

            if self.is_valid_move(new_pos):
                neighbors.append(new_pos)

        return neighbors

    def solve(self, start, goal):
        open_set = [(self.heuristic(start, goal), 0, start)]
        closed_set = set()
        g_scores = {start: 0}

        while open_set:
            _, cost, current = heapq.heappop(open_set)

            if current == goal:
                return cost

            if current in closed_set:
                continue

            closed_set.add(current)

            neighbors = self.generate_neighbors(current)

            for neighbor in neighbors:
                if neighbor not in closed_set:
                    tentative_g_score = g_scores[current] + 1

                    if neighbor not in g_scores or tentative_g_score < g_scores[neighbor]:
                        g_scores[neighbor] = tentative_g_score
                        heapq.heappush(open_set, (tentative_g_score + self.heuristic(neighbor, goal), tentative_g_score, neighbor))

        return None
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start_point = (0, 0)
goal_point = (4, 4)

astar = AStar(grid)
path_length = astar.solve(start_point, goal_point)

if path_length is not None:
    print(f"Shortest path length from {start_point} to {goal_point}: {path_length}")
else:
    print("No valid path found.")
