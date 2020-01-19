"""file to run our vacuum cleaning agents"""
from agents import (
    RandomizedReflexAgent)
from constants import ROOM, EMPTY
from environment import Environment
from experiment import Experiment


def single_run(agent, agent_name, env_type=EMPTY, print_grid=True):
    env_room = Environment(10, env_type)
    room_exp = Experiment(agent=agent, environment=env_room)
    (clean_cells, num_actions) = room_exp.run_experiment()
    if print_grid:
        print(f"Experiment on {agent_name} in `{env_type}` environment:")
        print(f"\tCells cleaned: {clean_cells}")
        print(f"\tActions taken: {num_actions}")
        print("Grid after experiment completion:")
        room_exp.print_grid()

    return clean_cells, num_actions


def multiple_runs(agent, agent_name, env_type=EMPTY, num_runs=50):
    list_of_simple_ratios = []
    list_of_derived_ratios = []
    list_of_num_actions = []
    while num_runs != 0:
        num_runs -= 1

        clean_cells, num_actions = single_run(agent, agent_name, env_type, print_grid=False)
        list_of_simple_ratios.append((float(clean_cells / num_actions)))
        list_of_derived_ratios.append((float(clean_cells / num_actions) * clean_cells))
        list_of_num_actions.append(num_actions)
    # print(f"average simple performance! {sum(list_of_simple_ratios) / len(list_of_simple_ratios)}")
    # print(f"average derived performance! {sum(list_of_derived_ratios) / len(list_of_derived_ratios)}")
    list_of_num_actions.sort()
    best_45 = list_of_num_actions[0:45]
    print(float(sum(best_45) / 45))
    # print(list_of_num_actions)


def main():
    print("--------------------------------------------")

    print("          Empty Grid Experiments")
    print("--------------------------------------------\n")
    # single_run(SimpleReflexAgent(), agent_name="Simple Reflex Agent", env_type=EMPTY)
    multiple_runs(RandomizedReflexAgent(), agent_name="Randomized Agent", env_type=EMPTY)
    # single_run(ModelBasedReflexAgent(), agent_name="Model Based Agent", env_type=EMPTY)

    print("--------------------------------------------")
    print("          ROOM Grid Experiments")
    print("--------------------------------------------\n")
    # single_run(SimpleReflexAgent(), agent_name="Simple Reflex Agent", env_type=ROOM)
    multiple_runs(RandomizedReflexAgent(), agent_name="Randomized Agent", env_type=ROOM)
    # single_run(ModelBasedReflexAgent(), agent_name="Model Based Agent", env_type=ROOM)


if __name__ == "__main__":
    main()
