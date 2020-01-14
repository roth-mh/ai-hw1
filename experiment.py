"""an experiment class to run the vacuum cleaning problem"""
from agents import RandomizedReflexAgent
from constants import NORTH, TURN, MOVE_FORWARD, CLEAN_SQUARE
from environment import Environment


class Experiment:
    def __init__(self, agent, grid):
        self.agent_x = 1
        self.agent_y = 1
        self.direction = NORTH
        self.agent = agent
        self.grid_object = grid
        self.num_actions = 0
        self.turns = 0

    def run_experiment(self):
        while (self.agent.is_active(self.agent_x, self.agent_y) or self.num_actions < 2) and self.turns < 150:
            self.turns += 1
            action_dict = self.agent.take_turn(self.grid_object, self.agent_x, self.agent_y, self.direction)
            if action_dict['action'] == TURN:
                self.num_actions += 1
                self.direction = action_dict['data']
            elif action_dict['action'] == CLEAN_SQUARE:
                self.num_actions += 1
            elif action_dict['action'] == MOVE_FORWARD:
                self.num_actions += 1
                self.agent_x = action_dict['data'][0]
                self.agent_y = action_dict['data'][1]

        self.agent.turn_off()
        self.num_actions += 1
        self.grid_object.print_grid()
        return self.grid_object.clean_cells, self.turns, self.num_actions


grid1 = Environment(10)
# agent1 = SimpleReflexAgent()
agent1 = RandomizedReflexAgent()
exp = Experiment(agent=agent1, grid=grid1)

print(exp.run_experiment())
