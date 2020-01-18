from constants import DIRTY, CLEAN, EMPTY


class Environment:
    def __init__(self, grid_size, env_type):
        self.grid_size = 10
        self.env_type = env_type
        self.dirty_cells = 10 * 10
        self.clean_cells = 0

        grid = [[DIRTY] * self.grid_size for _ in range(self.grid_size)]

        self.grid = grid

    def print_grid(self):
        """pretty prints a grid"""
        for i in range(len(self.grid) - 1, -1, -1):
            print(str(self.grid[i]) + '\n')

    def clean_cell(self, x, y):
        self.clean_cells += 1
        self.grid[x][y] = CLEAN


if __name__ == "__main__":
    room = Environment(10, EMPTY)
    room.print_grid()
