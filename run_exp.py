"""file to run our vacuum cleaning agents"""
import sys

from agents import (
    RandomizedReflexAgent, SimpleReflexAgent, ModelBasedReflexAgent)
from constants import EMPTY, ROOM, EMPTY_ENVIRONMENT, RANDOM_AGENT, MODEL_AGENT, SIMPLE_AGENT, ROOM_ENVIRONMENT
from environment import Environment
from experiment import Experiment


def single_run(agent, agent_name, env_type=EMPTY, print_grid=True):
    env_room = Environment(10, env_type)
    room_exp = Experiment(agent=agent, environment=env_room)
    (clean_cells, num_actions, list_of_clean_cells_at_each_step) = room_exp.run_experiment()
    if print_grid:
        print(f"Experiment on {agent_name} in `{env_type}` environment:")
        print(f"\tCells cleaned: {clean_cells}")
        print(f"\tActions taken: {num_actions}")
        # print("Grid after experiment completion:")
        # room_exp.print_grid()

    return clean_cells, num_actions, list_of_clean_cells_at_each_step


def multiple_runs(agent, agent_name, env_type=EMPTY, num_runs=50):
    list_of_simple_ratios = []
    list_of_derived_ratios = []
    list_of_num_actions = []
    all_clean_cells = []
    for i in range(0, 500):
        all_clean_cells.append([])
    while num_runs != 0:
        num_runs -= 1

        clean_cells, num_actions, list_of_clean_cells_at_each_step = single_run(agent, agent_name, env_type,
                                                                                print_grid=True)
        list_of_simple_ratios.append((float(clean_cells / num_actions)))
        list_of_derived_ratios.append((float(clean_cells / num_actions) * clean_cells))
        list_of_num_actions.append(num_actions)

        for i in range(len(all_clean_cells)):
            all_clean_cells[i].append(list_of_clean_cells_at_each_step[i])
    average_clean_cells = []
    for i in range(len(all_clean_cells)):
        average_clean_cells.append(sum(all_clean_cells[i]) / len(all_clean_cells[i]))
    return average_clean_cells


def main(agent, environment):
    if environment == EMPTY_ENVIRONMENT:
        print("--------------------------------------------")
        print("          Empty Grid Experiment")
        print("--------------------------------------------\n")
        if agent == RANDOM_AGENT:
            single_run(RandomizedReflexAgent(), agent_name="Randomized Agent", env_type=EMPTY)
        elif agent == MODEL_AGENT:
            single_run(ModelBasedReflexAgent(), agent_name="Model Based Agent", env_type=EMPTY)
        elif agent == SIMPLE_AGENT:
            single_run(SimpleReflexAgent(), agent_name="Simple Reflex Agent", env_type=EMPTY)

        else:
            print(f"ERROR; {agent} not in ['random', 'model', 'simple']")

    elif environment == ROOM_ENVIRONMENT:

        print("--------------------------------------------")
        print("          ROOM Grid Experiment")
        print("--------------------------------------------\n")
        if agent == SIMPLE_AGENT:
            single_run(SimpleReflexAgent(), agent_name="Simple Reflex Agent", env_type=ROOM)
        elif agent == RANDOM_AGENT:
            single_run(RandomizedReflexAgent(), agent_name="Randomized Agent", env_type=ROOM)
        elif agent == MODEL_AGENT:
            single_run(ModelBasedReflexAgent(), agent_name="Model Based Agent", env_type=ROOM)
        else:
            print(f"ERROR; {agent} not in ['random', 'model', 'simple']")
    else:
        print(f"ERROR; {environment} not in ['room', 'empty']")


if __name__ == "__main__":
    args = list(sys.argv)
    if len(sys.argv) > 3:
        print("ERROR; too many arguments")
    elif args[1].lower() not in ['random', 'simple', 'model']:
        print(f"{args[1]} not in ['random', 'simple', 'model']")
    elif args[2].lower() not in ['empty', 'room']:
        print(f"{args[2]} not in ['empty', 'room']")
    else:
        main(args[1].lower(), args[2].lower())
