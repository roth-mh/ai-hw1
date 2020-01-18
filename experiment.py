"""an experiment class to run the vacuum cleaning problem"""
from agents import SimpleReflexAgent, RandomizedReflexAgent, ModelBasedReflexAgentSimple, ModelBasedReflexAgent
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
        while self.num_actions < 500:
            self.num_actions += 1
            action_dict = self.agent.take_turn(self.environment, self.agent_x, self.agent_y, self.direction)
            if action_dict['action'] == TURN:
                self.direction = action_dict['data']
            elif action_dict['action'] == MOVE_FORWARD:
                self.agent_x = action_dict['data'][0]
                self.agent_y = action_dict['data'][1]
            elif action_dict['action'] == TURN_OFF:
                break

        return self.environment.clean_cells, self.num_actions
    
    def print_grid(self):
        self.environment.print_grid()


def single_run(agent, agent_name, env_type=EMPTY):
    env_room = Environment(10, env_type)
    room_exp = Experiment(agent=agent, environment=env_room)
    (clean_cells, num_actions) = room_exp.run_experiment()
    print(f"Experiment on {agent_name} in `{env_type}` environment:")
    print(f"\tCells cleaned: {clean_cells}")
    print(f"\tActions taken: {num_actions}")
    print("Grid after experiment completion:")
    room_exp.print_grid()


if __name__ == "__main__":
    print("--------------------------------------------")
    print("          Empty Grid Experiments")
    print("--------------------------------------------\n")
    single_run(SimpleReflexAgent(), agent_name="Simple Reflex Agent", env_type=EMPTY)
    single_run(RandomizedReflexAgent(), agent_name="Randomized Agent", env_type=EMPTY)
    single_run(ModelBasedReflexAgentSimple(), agent_name="Model Based Agent", env_type=EMPTY)
    single_run(ModelBasedReflexAgent(), agent_name="Model Based Agent 2", env_type=EMPTY)

    print("--------------------------------------------")
    print("          ROOM Grid Experiments")
    print("--------------------------------------------\n")
    single_run(SimpleReflexAgent(), agent_name="Simple Reflex Agent", env_type=ROOM)
    single_run(RandomizedReflexAgent(), agent_name="Randomized Agent", env_type=ROOM)
    single_run(ModelBasedReflexAgentSimple(), agent_name="Model Based Agent", env_type=ROOM)
    single_run(ModelBasedReflexAgent(), agent_name="Model Based Agent 2", env_type=ROOM)
