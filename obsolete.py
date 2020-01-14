"""An agent abstract class with the child classes below"""
from abc import ABC
from random import random

from constants import WALL, EAST, NORTH, WEST, SOUTH, DIRTY, MOVE_FORWARD, TURN, CLEAN_SQUARE


class Agent(ABC):

    def take_turn(self, grid_object, x, y, direction):
        pass

    def is_home(self, x_local, y_local):
        pass

    def turn_off(self):
        pass


class SimpleReflexAgent(Agent):
    """TODO: agent that only turns right regardless of direction (unknown)"""

    def __init__(self):
        self.num_actions = 0

    def clean_square(self, grid_object, x_local, y_local):
        """
        cleans a cell of the grid

        :param grid_object: the grid object
        :param x_local: the x location to be cleaned
        :param y_local: the y location to be cleaned
        :return:

        None
        """
        # grid[x_local][y_local] = CLEAN
        grid_object.clean_cell(x_local, y_local)
        self.num_actions += 1

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
            # self.clean_square(grid, x_local, y_local)
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
                print('direction is east')
                return True

        if direction == NORTH:
            if grid[x_local + 1][y_local] == WALL:
                print('direction is north')
                return True

        if direction == WEST:
            if grid[x_local][y_local - 1] == WALL:
                print('direction is west')
                return True

        if direction == SOUTH:
            if grid[x_local - 1][y_local] == WALL:
                print('direction is south')
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
        print('turning off')
        self.num_actions += 1
        return self.num_actions

    def move_forward(self, x, y, direction):
        """
        moves the agent forward by 1 cell in the direction it is facing

        :param x: the x coordinate of the agent
        :param y: the y coordinate of the agent
        :param direction: the direction the agent is facing
        :return:
            the new x, y coordinates of the agent
        """
        self.num_actions += 1
        if direction == EAST:
            return x, y + 1

        if direction == NORTH:
            return x + 1, y

        if direction == WEST:
            return x, y - 1

        if direction == SOUTH:
            return x - 1, y

    def turn(self, direction):
        """
        function that turns the direction of the agent 90 deg clockwise

        :param direction: the original direction of the agent
        :return:
            the new direction of the agent, or ERROR
        """
        self.num_actions += 1
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
            print('cleaning square')
            return {'action': CLEAN_SQUARE, 'data': None}

        elif self.is_wall(grid_object.grid, x, y, direction):
            new_direction = self.turn(direction)
            print(f'turning; new direction = {new_direction}')
            return {'action': TURN, 'data': new_direction}

        else:
            # r = random.randint(1)
            if random.randint(1) == 1:
                pass
            new_x, new_y = self.move_forward(x, y, direction)
            print(f'moving forward; new location: x = {new_x}, y = {new_y}')
            return {'action': MOVE_FORWARD, 'data': (new_x, new_y)}
