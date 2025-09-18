import random

def roulette_wheel_selection(population, fitness_list):
    """
    Selects one individual from the population using Roulette Wheel Selection.

    Args:
        population (list): List of individuals (can be any type).
        fitness_list (list of float): List of fitness values corresponding to each individual.

    Returns:
        object: Selected individual from the population.
    """
    if len(population) != len(fitness_list):
        raise ValueError("Population and fitness list must be the same length.")

    if any(f < 0 for f in fitness_list):
        raise ValueError("Fitness values must be non-negative.")

    total_fitness = sum(fitness_list)

    if total_fitness == 0:
        raise ValueError("Total fitness is zero. Cannot perform selection.")

    # Pick a random point in the fitness sum
    pick = random.uniform(0, total_fitness)
    current = 0

    # Find the individual where the pick falls
    for individual, fitness in zip(population, fitness_list):
        current += fitness
        if current >= pick:
            return individual

    # Fallback (due to float rounding issues)
    return population[-1]


# Example usage
if __name__ == "__main__":
    # Define a population (can be any data type)
    population = ['A', 'B', 'C', 'D']
    # Define their fitness values
    fitness_values = [10, 30, 50, 10]  # Total fitness = 100

    print("Roulette Wheel Selection Results:")
    # Perform selection multiple times to observe the probability distribution
    results = {}
    for _ in range(1000):
        selected = roulette_wheel_selection(population, fitness_values)
        if selected not in results:
            results[selected] = 0
        results[selected] += 1

    # Show how many times each individual was selected
    for individual in population:
        count = results.get(individual, 0)
        print(f"Individual {individual} selected {count} times ({(count/10):.1f}%)")
