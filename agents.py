"""An agent abstract class with the child classes below"""

import random
from abc import ABC

from constants import WALL, EAST, NORTH, WEST, SOUTH, DIRTY, MOVE_FORWARD, TURN, CLEAN_SQUARE, RIGHT, LEFT


class Agent(ABC):

    def take_turn(self, grid_object, x, y, direction):
        pass

    def is_active(self, x, y):
        pass

    # percepts:
    def is_home(self, x_local, y_local):
        pass

    def is_wall(self, grid, x_local, y_local, direction):
        pass

    def is_dirty(self, grid, x_local, y_local):
        pass

    def turn_off(self):
        pass


######################################
# Simple Reflex Agent ############
######################################

class SimpleReflexAgent(Agent):
    """TODO: agent that only turns right regardless of direction (unknown)"""
    """
    This shouldn't be considered 'memory' because the agent has no ability to store information
    it only uses that information atomically to make a decision (aka receives info from percept, 
    makes a move and 'forgets' what it just learned
    ...
    maybe it knows NORTH, EAST, SOUTH, and WEST? 
    """

    def __init__(self):
        pass

    def is_active(self, x, y):
        return not self.is_home(x_local=x, y_local=y)

    def clean_square(self, grid_object, x_local, y_local):
        """
        cleans a cell of the grid

        :param grid_object: the grid object
        :param x_local: the x location to be cleaned
        :param y_local: the y location to be cleaned
        :return:

        None
        """
        grid_object.clean_cell(x_local, y_local)

    def is_dirty(self, grid, x_local, y_local):
        """
        percept to see if the current cell is dirty

        :param grid: the grid, an nxn array, being used
        :param x_local: the x_location of the agent
        :param y_local: the y_location of the agent
        :return:
            True, if the location of the grid contains 'dirty'
            False, otherwise
        """
        if grid[x_local][y_local] == DIRTY:
            return True
        else:
            return False

    def is_wall(self, grid, x_local, y_local, direction):
        """
        percept to see if the agent is facing a wall

        :param grid: the grid, an nxn array, being used
        :param x_local: the x_location of the agent
        :param y_local: the y_location of the agent
        :param direction: the direction of the agent
        :return:
            True, if the agent is facing a wall
            False, otherwise
        """

        # TODO: check all directions
        if direction == EAST:
            if grid[x_local][y_local + 1] == WALL:
                # print('direction is east')
                return True

        if direction == NORTH:
            if grid[x_local + 1][y_local] == WALL:
                # print('direction is north')
                return True

        if direction == WEST:
            if grid[x_local][y_local - 1] == WALL:
                # print('direction is west')
                return True

        if direction == SOUTH:
            if grid[x_local - 1][y_local] == WALL:
                # print('direction is south')
                return True

        return False

    def is_home(self, x_local, y_local):
        """
        determines if an agent has reached the starting cell

        :param x_local: the agent's x location
        :param y_local: the agent's y location
        :return:
            True, if the agent is at the starting coordinates
            False, otherwise
        """
        if x_local == 1 and y_local == 1:
            return True
        else:
            return False

    def turn_off(self):
        """
        a function that concludes the agent's experiment by returning the # of actions

        :return:
            None
        """
        # print('turning off')
        return None

    def move_forward(self, x, y, direction):
        """
        moves the agent forward by 1 cell in the direction it is facing

        :param x: the x coordinate of the agent
        :param y: the y coordinate of the agent
        :param direction: the direction the agent is facing
        :return:
            the new x, y coordinates of the agent
        """
        if direction == EAST:
            return x, y + 1

        if direction == NORTH:
            return x + 1, y

        if direction == WEST:
            return x, y - 1

        if direction == SOUTH:
            return x - 1, y

    def turn_right(self, direction):
        """
        function that turns the direction of the agent 90 deg clockwise

        :param direction: the original direction of the agent
        :return:
            the new direction of the agent, or ERROR
        """
        if direction == NORTH:
            return EAST
        elif direction == EAST:
            return SOUTH
        elif direction == SOUTH:
            return WEST
        elif direction == WEST:
            return NORTH

        return 'ERROR'

    def take_turn(self, grid_object, x, y, direction):
        """
        a series of IF statements that dictates how the agent moves. (deterministic)

        :param grid_object: the grid object being used
        :param x: the x_location of the agent
        :param y: the y_location of the agent
        :param direction: the direction of the agent
        :return:
            a dictionary with one key communicating the action taken and the other any necessary data
        """
        if self.is_dirty(grid_object.grid, x, y):
            self.clean_square(grid_object, x, y)
            # print('cleaning square')
            return {'action': CLEAN_SQUARE, 'data': None}

        elif self.is_wall(grid_object.grid, x, y, direction):
            new_direction = self.turn_right(direction)
            # print(f'turning; new direction = {new_direction}')
            return {'action': TURN, 'data': new_direction}

        else:
            new_x, new_y = self.move_forward(x, y, direction)
            # print(f'moving forward; new location: x = {new_x}, y = {new_y}')
            return {'action': MOVE_FORWARD, 'data': (new_x, new_y)}


######################################
# Randomized Reflex Agent ############
######################################
class RandomizedReflexAgent(Agent):

    def __init__(self):
        pass

    def is_active(self, x, y):
        return True

    def clean_square(self, grid_object, x_local, y_local):
        """
        cleans a cell of the grid

        :param grid_object: the grid object
        :param x_local: the x location to be cleaned
        :param y_local: the y location to be cleaned
        :return:

        None
        """
        grid_object.clean_cell(x_local, y_local)

    def is_dirty(self, grid, x_local, y_local):
        """
        percept to see if the current cell is dirty

        :param grid: the grid, an nxn array, being used
        :param x_local: the x_location of the agent
        :param y_local: the y_location of the agent
        :return:
            True, if the location of the grid contains 'dirty'
            False, otherwise
        """
        if grid[x_local][y_local] == DIRTY:
            return True
        else:
            return False

    def is_wall(self, grid, x_local, y_local, direction):
        """
        percept to see if the agent is facing a wall

        :param grid: the grid, an nxn array, being used
        :param x_local: the x_location of the agent
        :param y_local: the y_location of the agent
        :param direction: the direction of the agent
        :return:
            True, if the agent is facing a wall
            False, otherwise
        """

        # TODO: check all directions
        if direction == EAST:
            if grid[x_local][y_local + 1] == WALL:
                # print('direction is east')
                return True

        if direction == NORTH:
            if grid[x_local + 1][y_local] == WALL:
                # print('direction is north')
                return True

        if direction == WEST:
            if grid[x_local][y_local - 1] == WALL:
                # print('direction is west')
                return True

        if direction == SOUTH:
            if grid[x_local - 1][y_local] == WALL:
                # print('direction is south')
                return True

        return False

    def is_home(self, x_local, y_local):
        """
        determines if an agent has reached the starting cell

        :param x_local: the agent's x location
        :param y_local: the agent's y location
        :return:
            True, if the agent is at the starting coordinates
            False, otherwise
        """
        if x_local == 1 and y_local == 1:
            return True
        else:
            return False

    def turn_off(self):
        """
        a function that concludes the agent's experiment by returning the # of actions

        :return:
            the agent's number of actions
        """
        # print('turning off')
        return True

    def move_forward(self, x, y, direction):
        """
        moves the agent forward by 1 cell in the direction it is facing

        :param x: the x coordinate of the agent
        :param y: the y coordinate of the agent
        :param direction: the direction the agent is facing
        :return:
            the new x, y coordinates of the agent
        """
        if direction == EAST:
            return x, y + 1

        if direction == NORTH:
            return x + 1, y

        if direction == WEST:
            return x, y - 1

        if direction == SOUTH:
            return x - 1, y

    def turn_right(self, direction):
        """
        function that turns the direction of the agent 90 deg clockwise

        :param direction: the original direction of the agent
        :return:
            the new direction of the agent, or ERROR
        """
        if direction == NORTH:
            return EAST
        elif direction == EAST:
            return SOUTH
        elif direction == SOUTH:
            return WEST
        elif direction == WEST:
            return NORTH

        return 'ERROR'

    def turn_left(self, direction):
        """
        function that turns the direction of the agent 90 deg counterclockwise

        :param direction: the original direction of the agent
        :return:
            the new direction of the agent, or ERROR
        """
        if direction == NORTH:
            return EAST
        elif direction == EAST:
            return SOUTH
        elif direction == SOUTH:
            return WEST
        elif direction == WEST:
            return NORTH

        return 'ERROR'

    def take_turn(self, grid_object, x, y, direction):
        """
        a series of IF statements that dictates how the agent moves. (deterministic)

        :param grid_object: the grid object being used
        :param x: the x_location of the agent
        :param y: the y_location of the agent
        :param direction: the direction of the agent
        :return:
            a dictionary with one key communicating the action taken and the other any necessary data
        """
        if self.is_dirty(grid_object.grid, x, y):
            self.clean_square(grid_object, x, y)
            # print('cleaning square')
            return {'action': CLEAN_SQUARE, 'data': None}

        elif self.is_wall(grid_object.grid, x, y, direction):
            if random.randint(0, 1) == 1:
                # print('turning right')
                new_direction = self.turn_right(direction)
            else:
                # print('turning left')
                new_direction = self.turn_left(direction)

            # print(f'turning; new direction = {new_direction}')
            return {'action': TURN, 'data': new_direction}

        else:
            new_x, new_y = self.move_forward(x, y, direction)
            # print(f'moving forward; new location: x = {new_x}, y = {new_y}')
            return {'action': MOVE_FORWARD, 'data': (new_x, new_y)}


######################################
# Model Based Reflex Agent ###########
######################################
class ModelBasedReflexAgent(Agent):

    def __init__(self):
        self.turn_direction = RIGHT
        self.just_saw_wall = False

    def is_active(self, x, y):
        return True

    def clean_square(self, grid_object, x_local, y_local):
        """
        cleans a cell of the grid

        :param grid_object: the grid object
        :param x_local: the x location to be cleaned
        :param y_local: the y location to be cleaned
        :return:

        None
        """
        grid_object.clean_cell(x_local, y_local)

    def is_dirty(self, grid, x_local, y_local):
        """
        percept to see if the current cell is dirty

        :param grid: the grid, an nxn array, being used
        :param x_local: the x_location of the agent
        :param y_local: the y_location of the agent
        :return:
            True, if the location of the grid contains 'dirty'
            False, otherwise
        """
        if grid[x_local][y_local] == DIRTY:
            return True
        else:
            return False

    def is_wall(self, grid, x_local, y_local, direction):
        """
        percept to see if the agent is facing a wall

        :param grid: the grid, an nxn array, being used
        :param x_local: the x_location of the agent
        :param y_local: the y_location of the agent
        :param direction: the direction of the agent
        :return:
            True, if the agent is facing a wall
            False, otherwise
        """

        # TODO: check all directions
        if direction == EAST:
            if grid[x_local][y_local + 1] == WALL:
                # print('direction is east')
                return True

        if direction == NORTH:
            if grid[x_local + 1][y_local] == WALL:
                # print('direction is north')
                return True

        if direction == WEST:
            if grid[x_local][y_local - 1] == WALL:
                # print('direction is west')
                return True

        if direction == SOUTH:
            if grid[x_local - 1][y_local] == WALL:
                # print('direction is south')
                return True

        return False

    def is_home(self, x_local, y_local):
        """
        determines if an agent has reached the starting cell

        :param x_local: the agent's x location
        :param y_local: the agent's y location
        :return:
            True, if the agent is at the starting coordinates
            False, otherwise
        """
        if x_local == 1 and y_local == 1:
            return True
        else:
            return False

    def turn_off(self):
        """
        a function that concludes the agent's experiment by returning the # of actions

        :return:
            the agent's number of actions
        """
        # print('turning off')
        return True

    def move_forward(self, x, y, direction):
        """
        moves the agent forward by 1 cell in the direction it is facing

        :param x: the x coordinate of the agent
        :param y: the y coordinate of the agent
        :param direction: the direction the agent is facing
        :return:
            the new x, y coordinates of the agent
        """
        if direction == EAST:
            return x, y + 1

        if direction == NORTH:
            return x + 1, y

        if direction == WEST:
            return x, y - 1

        if direction == SOUTH:
            return x - 1, y

    def turn_right(self, direction):
        """
        function that turns the direction of the agent 90 deg clockwise

        :param direction: the original direction of the agent
        :return:
            the new direction of the agent, or ERROR
        """
        if direction == NORTH:
            return EAST
        elif direction == EAST:
            return SOUTH
        elif direction == SOUTH:
            return WEST
        elif direction == WEST:
            return NORTH

        return 'ERROR'

    def turn_left(self, direction):
        """
        function that turns the direction of the agent 90 deg counterclockwise

        :param direction: the original direction of the agent
        :return:
            the new direction of the agent, or ERROR
        """
        if direction == NORTH:
            return EAST
        elif direction == EAST:
            return SOUTH
        elif direction == SOUTH:
            return WEST
        elif direction == WEST:
            return NORTH

        return 'ERROR'

    def take_turn(self, grid_object, x, y, direction):
        """
        a series of IF statements that dictates how the agent moves. (deterministic)

        :param grid_object: the grid object being used
        :param x: the x_location of the agent
        :param y: the y_location of the agent
        :param direction: the direction of the agent
        :return:
            a dictionary with one key communicating the action taken and the other any necessary data
        """
        if self.just_saw_wall and self.is_dirty(grid_object.grid, x, y):
            if self.turn_direction == RIGHT:
                new_direction = self.turn_right(direction)
                self.turn_direction = LEFT

            else:  # if self.turn_direction == LEFT:
                new_direction = self.turn_left(direction)
                self.turn_direction = RIGHT

            self.just_saw_wall = False
            return {'action': TURN, 'data': new_direction}

        elif self.is_dirty(grid_object.grid, x, y):
            self.clean_square(grid_object, x, y)
            return {'action': CLEAN_SQUARE, 'data': None}

        elif self.is_wall(grid_object.grid, x, y, direction):
            if self.turn_direction == RIGHT:
                new_direction = self.turn_right(direction)
            else:  # if self.turn_direction == LEFT:
                new_direction = self.turn_left(direction)

            self.just_saw_wall = True
            return {'action': TURN, 'data': new_direction}

        else:
            new_x, new_y = self.move_forward(x, y, direction)
            return {'action': MOVE_FORWARD, 'data': (new_x, new_y)}
