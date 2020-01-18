"""An agent abstract class with the child classes below"""

import random
from abc import ABC

from constants import (
    EAST,
    NORTH,
    WEST,
    SOUTH,
    DIRTY,
    MOVE_FORWARD,
    TURN,
    CLEAN_SQUARE,
    RIGHT,
    LEFT,
    TURN_OFF,
    ROOM,
)


class Agent(ABC):
    def take_turn(self, grid_object, x, y, direction):
        pass

    # percepts:
    def is_home(self, x, y):
        """
        determines if an agent has reached the starting cell

        :param x: the agent's x location
        :param y: the agent's y location
        :return:
            True, if the agent is at the starting coordinates
            False, otherwise
        """
        if x == 0 and y == 0:
            return True
        else:
            return False

    def is_wall(self, grid_obj, x, y, direction):
        """
        percept to see if the agent is facing a wall

        :param grid_obj: the grid, an nxn array, being used
        :param x: the x_location of the agent
        :param y: the y_location of the agent
        :param direction: the direction of the agent
        :return:
            True, if the agent is facing a wall
            False, otherwise
        """

        if grid_obj.env_type == ROOM:

            # the four rooms:

            # door 1
            if x == 0 and y == 4 and direction == EAST:
                return False
            if x == 0 and y == 5 and direction == WEST:
                return False

            # door 2
            if x == 4 and y == 0 and direction == NORTH:
                return False
            if x == 5 and y == 0 and direction == SOUTH:
                return False

            # door 3
            if x == 9 and y == 4 and direction == EAST:
                return False
            if x == 9 and y == 5 and direction == WEST:
                return False

            # door 4
            if x == 4 and y == 9 and direction == NORTH:
                return False
            if x == 5 and y == 9 and direction == SOUTH:
                return False

            if x == 4 and direction == NORTH:
                return True
            if x == 5 and direction == SOUTH:
                return True
            if y == 4 and direction == EAST:
                return True
            if x == 5 and direction == WEST:
                return True

        if x == 0 and direction == SOUTH:
            return True
        if y == 0 and direction == WEST:
            return True
        if x == 9 and direction == NORTH:
            return True
        if y == 9 and direction == EAST:
            return True

        return False

    def is_dirty(self, grid, x, y):
        """
        percept to see if the current cell is dirty

        :param grid: the grid, an nxn array, being used
        :param x: the x_location of the agent
        :param y: the y_location of the agent
        :return:
            True, if the location of the grid contains 'dirty'
            False, otherwise
        """
        if grid[x][y] == DIRTY:
            return True
        else:
            return False

    def turn_right(self, grid_object=None, x=-1, y=-1, direction=None):
        """
        function that turns the direction of the agent 90 deg clockwise

        :param direction: the original direction of the agent
        :return:
            the new direction of the agent, or ERROR
        """
        new_direction = direction
        if direction == NORTH:
            new_direction = EAST
        elif direction == EAST:
            new_direction = SOUTH
        elif direction == SOUTH:
            new_direction = WEST
        elif direction == WEST:
            new_direction = NORTH

        return {"action": TURN, "data": new_direction}

    def turn_left(self, grid_object=None, x=-1, y=-1, direction=None):
        """
        function that turns the direction of the agent 90 deg counterclockwise

        :param direction: the original direction of the agent
        :return:
            the new direction of the agent, or ERROR
        """
        new_direction = direction
        if direction == NORTH:
            new_direction = WEST
        elif direction == EAST:
            new_direction = NORTH
        elif direction == SOUTH:
            new_direction = EAST
        elif direction == WEST:
            new_direction = SOUTH

        return {"action": TURN, "data": new_direction}

    def clean_square(self, grid_object=None, x=-1, y=-1, direction=None):
        """
        cleans a cell of the grid

        :param grid_object: the grid object
        :param x: the x location to be cleaned
        :param y: the y location to be cleaned
        :return:

        None
        """
        grid_object.clean_cell(x, y)
        return {"action": CLEAN_SQUARE, "data": None}

    def turn_off(self, grid_object=None, x=-1, y=-1, direction=None):
        """
        a function that concludes the agent's experiment by returning the # of actions

        :return:
            True
        """
        return {"action": TURN_OFF, "data": None}

    def move_forward(self, grid_object=None, x=-1, y=-1, direction=None):
        """
        moves the agent forward by 1 cell in the direction it is facing

        :param x: the x coordinate of the agent
        :param y: the y coordinate of the agent
        :param direction: the direction the agent is facing
        :return:
            the new x, y coordinates of the agent
        """
        new_x = x
        new_y = y

        if direction == EAST:
            new_y += 1

        if direction == NORTH:
            new_x += 1

        if direction == WEST:
            new_y -= 1

        if direction == SOUTH:
            new_x -= 1

        return {"action": MOVE_FORWARD, "data": (new_x, new_y)}


######################################
# Simple Reflex Agent ################
######################################
class SimpleReflexAgent(Agent):
    def __init__(self):
        pass

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
        is_dirty = self.is_dirty(grid_object.grid, x, y)
        is_home = self.is_home(x, y)
        is_wall = self.is_wall(grid_object, x, y, direction)

        if is_dirty:
            return self.clean_square(grid_object=grid_object, x=x, y=y)

        if is_home and is_wall:
            return self.turn_off()

        if is_wall:
            return self.turn_right(direction=direction)

        if not is_wall:
            return self.move_forward(x=x, y=y, direction=direction)


######################################
# Randomized Reflex Agent ############
######################################
class RandomizedReflexAgent(Agent):
    def __init__(self):
        pass

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
            return self.clean_square(grid_object=grid_object, x=x, y=y)
        elif self.is_wall(grid_object, x, y, direction=direction):
            if random.randint(0, 1) == 1:
                return self.turn_right(direction=direction)
            else:
                return self.turn_left(direction=direction)
        else:
            if random.randint(0, 10) >= 8:
                if random.randint(0, 1) == 1:
                    return self.turn_right(direction=direction)
                else:
                    return self.turn_left(direction=direction)
            return self.move_forward(x=x, y=y, direction=direction)


######################################
# Model Based Reflex Agent ###########
######################################
class ModelBasedReflexAgentSimple(Agent):
    def __init__(self):
        self.turn_direction = RIGHT  # either RIGHT or LEFT
        self.just_saw_wall = False

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
        is_wall = self.is_wall(grid_object, x, y, direction)
        is_dirty = self.is_dirty(grid_object.grid, x, y)

        if self.just_saw_wall and is_wall and not is_dirty:
            return self.turn_off()

        if self.just_saw_wall and is_dirty and self.turn_direction == RIGHT:
            self.just_saw_wall = False
            self.turn_direction = LEFT
            return self.turn_right(direction=direction)

        if self.just_saw_wall and is_dirty and not self.turn_direction == RIGHT:
            self.just_saw_wall = False
            self.turn_direction = RIGHT
            return self.turn_left(direction=direction)

        if is_dirty:
            return self.clean_square(grid_object=grid_object, x=x, y=y)

        if is_wall and self.turn_direction == RIGHT:
            self.just_saw_wall = True
            return self.turn_right(direction=direction)

        if is_wall and not self.turn_direction == RIGHT:
            self.just_saw_wall = True
            return self.turn_left(direction=direction)

        if not is_wall:
            return self.move_forward(x=x, y=y, direction=direction)


######################################
# Model Based Reflex Agent ###########
######################################
class ModelBasedReflexAgent(Agent):
    def __init__(self):
        self.memory = (0, 0, 0)

    def take_turn(self, grid_object, x, y, direction):
        """
        a sequence of IF statements that dictates how the agent moves. (deterministic)

        :param grid_object: the grid object being used
        :param x: the x_location of the agent
        :param y: the y_location of the agent
        :param direction: the direction of the agent
        :return:
            a dictionary with one key communicating the action taken and the other any necessary data
        """
        internal_state = (
            int(self.is_dirty(grid_object.grid, x, y)),
            int(self.is_home(x, y)),
            int(self.is_wall(grid_object, x, y, direction)),
            self.memory[0],
            self.memory[1],
            self.memory[2],
        )
        rules = [
            # internal state -> [new memory, action_func]
            [(1, 0, 0, 1, 0, 0), (1, 0, 0), self.clean_square],
            [(1, 0, 1, 1, 0, 0), (1, 0, 0), self.clean_square],
            [(1, 1, 0, 1, 0, 0), (1, 0, 0), self.clean_square],
            [(1, 1, 1, 1, 0, 0), (1, 0, 0), self.clean_square],
            [(1, 0, 0, 0, 0, 0), (0, 0, 0), self.clean_square],
            [(1, 0, 1, 0, 0, 0), (0, 0, 0), self.clean_square],
            [(1, 1, 0, 0, 0, 0), (0, 0, 0), self.clean_square],
            [(1, 1, 1, 0, 0, 0), (0, 0, 0), self.clean_square],
            [(1, 0, 0, 0, 0, 1), (0, 0, 1), self.clean_square],
            [(1, 0, 1, 0, 0, 1), (0, 0, 1), self.clean_square],
            [(1, 0, 0, 1, 0, 1), (1, 0, 1), self.clean_square],
            [(1, 0, 1, 1, 0, 1), (1, 0, 1), self.clean_square],
            [(0, 0, 0, 0, 0, 0), (0, 0, 0), self.move_forward],
            [(0, 1, 0, 0, 0, 0), (0, 0, 0), self.move_forward],
            [(0, 0, 0, 1, 0, 0), (1, 0, 0), self.move_forward],
            [(0, 1, 0, 1, 0, 0), (1, 0, 0), self.move_forward],
            [(0, 0, 0, 0, 1, 0), (0, 0, 1), self.move_forward],
            [(0, 1, 0, 0, 1, 0), (0, 0, 1), self.move_forward],
            [(0, 0, 0, 1, 1, 0), (1, 0, 1), self.move_forward],
            [(0, 1, 0, 1, 1, 0), (1, 0, 1), self.move_forward],
            [(0, 0, 1, 1, 1, 0), (0, 1, 1), self.turn_right],
            [(0, 0, 1, 0, 1, 1), (0, 1, 0), self.turn_right],
            [(0, 0, 1, 0, 0, 0), (0, 1, 0), self.turn_right],
            [(0, 0, 0, 0, 0, 1), (1, 0, 0), self.turn_right],
            [(0, 0, 1, 0, 0, 1), (1, 0, 0), self.turn_right],
            [(0, 1, 0, 0, 0, 1), (1, 0, 0), self.turn_right],
            [(0, 0, 1, 1, 0, 0), (1, 1, 0), self.turn_left],
            [(0, 0, 0, 1, 0, 1), (0, 0, 0), self.turn_left],
            [(0, 0, 1, 1, 0, 1), (0, 0, 0), self.turn_left],
            [(0, 1, 0, 1, 0, 1), (0, 0, 0), self.turn_left],
            [(0, 1, 1, 0, 0, 0), (0, 1, 1), self.turn_off],
            [(0, 1, 1, 0, 0, 1), (0, 1, 1), self.turn_off],
            [(0, 1, 1, 0, 1, 0), (0, 1, 1), self.turn_off],
            [(0, 1, 1, 0, 1, 1), (0, 1, 1), self.turn_off],
            [(0, 1, 1, 1, 0, 0), (0, 1, 1), self.turn_off],
            [(0, 1, 1, 1, 0, 1), (0, 1, 1), self.turn_off],
            [(0, 1, 1, 1, 1, 0), (0, 1, 1), self.turn_off],
            [(0, 1, 1, 1, 1, 1), (0, 1, 1), self.turn_off],
        ]

        for if_then_rule in rules:
            if internal_state == if_then_rule[0]:
                self.memory = if_then_rule[1]
                return if_then_rule[2](
                    grid_object=grid_object, x=x, y=y, direction=direction
                )
