import random

def roulette_wheel_selection(population, fitness_list):
   
    if len(population) != len(fitness_list):
        raise ValueError("Population and fitness list must be the same length.")

    if any(f < 0 for f in fitness_list):
        raise ValueError("Fitness values must be non-negative.")

    total_fitness = sum(fitness_list)

    if total_fitness == 0:
        raise ValueError("Total fitness is zero. Cannot perform selection.")


    pick = random.uniform(0, total_fitness)
    current = 0


    for individual, fitness in zip(population, fitness_list):
        current += fitness
        if current >= pick:
            return individual

 
    return population[-1]



if __name__ == "__main__":

    population = ['A', 'B', 'C', 'D']

    fitness_values = [10, 30, 50, 10] 

    print("Roulette Wheel Selection Results:")

    results = {}
    for _ in range(1000):
        selected = roulette_wheel_selection(population, fitness_values)
        if selected not in results:
            results[selected] = 0
        results[selected] += 1


    for individual in population:
        count = results.get(individual, 0)
        print(f"Individual {individual} selected {count} times ({(count/10):.1f}%)")
