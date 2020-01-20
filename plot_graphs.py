import matplotlib.pyplot as plt
import pandas as pd


def plot_relation(random_agent, simple_agent, model_agent, env_type):
    while len(simple_agent) != 500:
        simple_agent.append(36)

    while len(model_agent) != 500:
        model_agent.append(100)

    df = pd.DataFrame({'x': range(1, 501), 'random': random_agent, 'simple': simple_agent, 'model': model_agent})

    plt.plot('x', 'random', data=df, marker='', color='red', linewidth=2)
    plt.plot('x', 'simple', data=df, marker='', color='blue', linewidth=2)
    plt.plot('x', 'model', data=df, marker='', color='olive', linewidth=2)
    plt.ylabel('cleaned cells')
    plt.xlabel('number of actions')
    plt.title(f'Agents in {env_type}')
    plt.legend()
    plt.show()
    return
