"""file to run our vacuum cleaning agents"""
from agents import (
    SimpleReflexAgent,
    RandomizedReflexAgent,
    ModelBasedReflexAgentSimple,
    ModelBasedReflexAgent,
)
from constants import ROOM, EMPTY
from environment import Environment
from experiment import Experiment


def single_run(agent, agent_name, env_type=EMPTY):
    env_room = Environment(10, env_type)
    room_exp = Experiment(agent=agent, environment=env_room)
    (clean_cells, num_actions) = room_exp.run_experiment()
    print(f"Experiment on {agent_name} in `{env_type}` environment:")
    print(f"\tCells cleaned: {clean_cells}")
    print(f"\tActions taken: {num_actions}")
    print("Grid after experiment completion:")
    room_exp.print_grid()


def main():
    print("--------------------------------------------")
    print("          Empty Grid Experiments")
    print("--------------------------------------------\n")
    single_run(SimpleReflexAgent(), agent_name="Simple Reflex Agent", env_type=EMPTY)
    single_run(RandomizedReflexAgent(), agent_name="Randomized Agent", env_type=EMPTY)
    single_run(ModelBasedReflexAgent(), agent_name="Model Based Agent", env_type=EMPTY)

    print("--------------------------------------------")
    print("          ROOM Grid Experiments")
    print("--------------------------------------------\n")
    single_run(SimpleReflexAgent(), agent_name="Simple Reflex Agent", env_type=ROOM)
    single_run(RandomizedReflexAgent(), agent_name="Randomized Agent", env_type=ROOM)
    single_run(ModelBasedReflexAgent(), agent_name="Model Based Agent", env_type=ROOM)


if __name__ == "__main__":
    main()
