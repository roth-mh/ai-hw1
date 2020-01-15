from constants import WALL, DIRTY, CLEAN, EMPTY, ROOM


class Environment:
    def __init__(self, grid_size, env_type):
        self.grid_size = grid_size
        self.env_type = env_type
        self.dirty_cells = grid_size * grid_size
        self.clean_cells = 0

        if env_type == EMPTY:
            """makes a square array with the outer edges being walls"""
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
        elif env_type == ROOM:
            """makes a roomed environment"""
            grid = [[''] * (self.grid_size + 2) for _ in range(self.grid_size + 2)]
            quarter = ((self.grid_size + 2) / 4)
            first_door = quarter
            second_door = quarter * 3
            for x in range(self.grid_size + 2):
                for y in range(self.grid_size + 2):
                    if x > 0 and self.grid_size / x == 2:
                        if y == first_door or y == second_door:
                            grid[x][y] = DIRTY
                        else:
                            grid[x][y] = WALL
                    elif y > 0 and self.grid_size / y == 2:
                        if x == first_door or x == second_door:
                            grid[x][y] = DIRTY
                        else:
                            grid[x][y] = WALL
                    elif x == 0 or x == self.grid_size + 1:
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


# room = Environment(10, ROOM)
# room.print_grid()
