"""file to run our vacuum cleaning agents"""
from agents import (
    RandomizedReflexAgent, SimpleReflexAgent, ModelBasedReflexAgent)
from constants import EMPTY, ROOM
from environment import Environment
from experiment import Experiment
from plot_graphs import plot_relation


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


def main():
    print("--------------------------------------------")

    print("          Empty Grid Experiments")
    print("--------------------------------------------\n")
    cells, actions, simple_metrics = single_run(SimpleReflexAgent(), agent_name="Simple Reflex Agent", env_type=EMPTY)
    random_metrics = multiple_runs(RandomizedReflexAgent(), agent_name="Randomized Agent", env_type=EMPTY)
    cells, actions, model_metrics = single_run(ModelBasedReflexAgent(), agent_name="Model Based Agent", env_type=EMPTY)
    plot_relation(random_metrics, simple_metrics, model_metrics, "Empty Environment")

    print("--------------------------------------------")
    print("          ROOM Grid Experiments")
    print("--------------------------------------------\n")
    cells, actions, simple_room_metrics = single_run(SimpleReflexAgent(), agent_name="Simple Reflex Agent",
                                                     env_type=ROOM)
    random_room_metrics = multiple_runs(RandomizedReflexAgent(), agent_name="Randomized Agent", env_type=ROOM)
    cells, actions, model_room_metrics = single_run(ModelBasedReflexAgent(), agent_name="Model Based Agent",
                                                    env_type=ROOM)

    plot_relation(random_room_metrics, simple_room_metrics, model_room_metrics, "Room Environment")


if __name__ == "__main__":
    main()
