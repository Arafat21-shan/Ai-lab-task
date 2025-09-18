import random

def fitness_fn(x):
    
    return -x**2 + 10*x

def successor_fn(x):
   
    step = 1
    return [x - step, x + step]

def local_beam_search(initial_states, successor_fn, fitness_fn, k=3, max_iterations=10):
   

    beam = initial_states

    print(f"Initial states: {beam}")
    print(f"Initial fitness: {[fitness_fn(s) for s in beam]}")

    for iteration in range(max_iterations):
        print(f"\n--- Iteration {iteration + 1} ---")

 
        successors = []
        for state in beam:
            new_states = successor_fn(state)
            successors.extend(new_states)

  
        all_candidates = beam + successors


        all_candidates = list(set(all_candidates))

        
        all_candidates.sort(key=fitness_fn, reverse=True)

       
        beam = all_candidates[:k]

 
        print(f"Current beam: {beam}")
        print(f"Fitness: {[fitness_fn(s) for s in beam]}")


    best_state = beam[0]
    return best_state, fitness_fn(best_state)


if __name__ == "__main__":
 
    initial_states = [random.randint(0, 10) for _ in range(3)]

   
    beam_width = 3
    max_iters = 10

    best_state, best_fitness = local_beam_search(
        initial_states,
        successor_fn,
        fitness_fn,
        k=beam_width,
        max_iterations=max_iters
    )

    print(f"\n🏁 Final best state: {best_state}, Fitness: {best_fitness}")
