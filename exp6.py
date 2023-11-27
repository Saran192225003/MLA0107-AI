class VacuumCleaner:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.current_position = (0, 0)

    def print_grid(self):
        for row in self.grid:
            print(" ".join(map(str, row)))
        print()

    def move_up(self):
        if self.current_position[0] > 0:
            self.current_position = (self.current_position[0] - 1, self.current_position[1])

    def move_down(self):
        if self.current_position[0] < self.rows - 1:
            self.current_position = (self.current_position[0] + 1, self.current_position[1])

    def move_left(self):
        if self.current_position[1] > 0:
            self.current_position = (self.current_position[0], self.current_position[1] - 1)

    def move_right(self):
        if self.current_position[1] < self.cols - 1:
            self.current_position = (self.current_position[0], self.current_position[1] + 1)

    def clean_current_cell(self):
        if self.grid[self.current_position[0]][self.current_position[1]] == 1:
            self.grid[self.current_position[0]][self.current_position[1]] = 0

    def clean_all_cells(self):
        while any(1 in row for row in self.grid):
            self.print_grid()
            self.clean_current_cell()

            # Move to the next dirty cell
            if any(1 in row for row in self.grid[self.current_position[0] + 1:]):
                self.move_down()
            elif any(1 in row for row in self.grid[self.current_position[0] - 1::-1]):
                self.move_up()
            elif 1 in self.grid[self.current_position[0]][self.current_position[1] + 1:]:
                self.move_right()
            elif 1 in self.grid[self.current_position[0]][:self.current_position[1]][::-1]:
                self.move_left()

if __name__ == "__main__":
    # Example grid (1 represents dirty cell, 0 represents clean cell)
    grid = [
        [1, 0, 1, 0, 1],
        [0, 0, 1, 0, 0],
        [1, 1, 1, 1, 1],
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
    ]

    vacuum_cleaner = VacuumCleaner(grid)
    vacuum_cleaner.clean_all_cells()
