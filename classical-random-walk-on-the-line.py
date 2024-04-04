import random
import matplotlib.pyplot as plt
from typing import Dict, Tuple, List


PROBABILITY_THRESHOLD = 0.5


def random_walk_on_the_line(steps: int) -> int:
    position = 0
    for _ in range(steps):
        if random.uniform(0, 1) < PROBABILITY_THRESHOLD:
            position -= 1
        else:
            position += 1
    return position


def monte_carlo_simulation(number_of_executions: int = 1000, walk_steps: int = 100) -> Dict[int, int]:
    results = {}
    for _ in range(number_of_executions):
        result = random_walk_on_the_line(walk_steps)
        results[result] = results.get(result, 0) + 1
    return results


def prepare_results_for_plotting(dictionary: Dict[int, int]) -> Tuple[List[int], List[int]]:
    positions = []
    number_of_occurance = []
    for key, value in dictionary.items():
        positions.append(key)
        number_of_occurance.append(value)
    return positions, number_of_occurance


def plot_results(dictionary: Dict[int, int]) -> None:
    positions, number_of_occurance = prepare_results_for_plotting(dictionary)
    plt.bar(positions, number_of_occurance)
    plt.ylabel('number of occurances')
    plt.xlabel('positions')
    plt.show()


simulation_results = monte_carlo_simulation(100000, 100)
plot_results(simulation_results)
