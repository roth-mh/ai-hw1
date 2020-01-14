from constants import WALL, DIRTY, CLEAN


class Environment:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.dirty_cells = grid_size * grid_size
        self.clean_cells = 0

        """makes an square array with the outer edges being walls"""
        grid = [[''] * (self.grid_size + 2) for _ in range(self.grid_size + 2)]
        for x in range(self.grid_size + 2):
            for y in range(self.grid_size + 2):
                if x == 0 or x == self.grid_size + 1:
                    grid[x][y] = WALL
                elif y == 0 or y == self.grid_size + 1:
                    grid[x][y] = WALL
                else:
                    grid[x][y] = DIRTY

        self.grid = grid

    def print_grid(self):
        """pretty prints a grid"""
        for i in range(len(self.grid) - 1, -1, -1):
            print(str(self.grid[i]) + '\n')

    def clean_cell(self, x, y):
        self.clean_cells += 1
        self.grid[x][y] = CLEAN

# if __name__ == "__main__":
#     print_grid(make_grid(10))
