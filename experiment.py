"""an experiment class to run the vacuum cleaning problem"""
from agents import SimpleReflexAgent, RandomizedReflexAgent, ModelBasedReflexAgent
from constants import NORTH, TURN, MOVE_FORWARD, CLEAN_SQUARE, ROOM, EMPTY, TURN_OFF
from environment import Environment


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
        while self.turns < 200:
            self.turns += 1
            action_dict = self.agent.take_turn(self.environment, self.agent_x, self.agent_y, self.direction)
            if action_dict['action'] == TURN:
                self.num_actions += 1
                self.direction = action_dict['data']
            elif action_dict['action'] == CLEAN_SQUARE:
                self.num_actions += 1
            elif action_dict['action'] == MOVE_FORWARD:
                self.num_actions += 1
                self.agent_x = action_dict['data'][0]
                self.agent_y = action_dict['data'][1]
                print(f"new x: {self.agent_x}, new y: {self.agent_y}")
            elif action_dict['action'] == TURN_OFF:
                self.num_actions += 1
                break

        # self.agent.turn_off()
        self.num_actions += 1
        self.environment.print_grid()
        return self.environment.clean_cells, self.turns, self.num_actions


agent1 = SimpleReflexAgent()
agent2 = RandomizedReflexAgent()
agent3 = ModelBasedReflexAgent()

env_room = Environment(10, ROOM)
room_exp = Experiment(agent=agent3, environment=env_room)

env_grid = Environment(10, EMPTY)
grid_exp = Experiment(agent=agent1, environment=env_grid)

print(f"ROOM experiment on randomized agent results: {room_exp.run_experiment()}")

# print(f"GRID experiment on randomized agent results: {grid_exp.run_experiment()}")
