"""an experiment class to run the vacuum cleaning problem"""
from constants import NORTH, TURN, MOVE_FORWARD, TURN_OFF


class Experiment:
    def __init__(self, agent, environment):
        self.agent_x = 0
        self.agent_y = 0
        self.direction = NORTH
        self.agent = agent
        self.environment = environment
        self.num_actions = 0
        self.turns = 0

    def run_experiment(self):
        while self.environment.clean_cells < 89:
            self.num_actions += 1
            action_dict = self.agent.take_turn(
                self.environment, self.agent_x, self.agent_y, self.direction
            )
            if action_dict["action"] == TURN:
                self.direction = action_dict["data"]
            elif action_dict["action"] == MOVE_FORWARD:
                self.agent_x = action_dict["data"][0]
                self.agent_y = action_dict["data"][1]
            elif action_dict["action"] == TURN_OFF:
                break

        return self.environment.clean_cells, self.num_actions

    def print_grid(self):
        self.environment.print_grid()
