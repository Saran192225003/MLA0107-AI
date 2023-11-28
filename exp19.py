import math
import random

def objective_function(x):
    # Define your objective function to be minimized
    return x**2 + 5 * math.sin(x)

def simulated_annealing(initial_solution, temperature, cooling_rate, iterations):
    current_solution = initial_solution
    current_energy = objective_function(current_solution)

    for _ in range(iterations):
        # Generate a neighboring solution
        neighbor_solution = current_solution + random.uniform(-0.5, 0.5)

        # Evaluate the energy of the neighboring solution
        neighbor_energy = objective_function(neighbor_solution)

        # Calculate the probability of accepting the neighbor solution
        acceptance_probability = min(1, math.exp(-(neighbor_energy - current_energy) / temperature))

        # Decide whether to move to the neighbor solution
        if random.uniform(0, 1) < acceptance_probability:
            current_solution = neighbor_solution
            current_energy = neighbor_energy

        # Cool down the temperature
        temperature *= cooling_rate

    return current_solution, objective_function(current_solution)

def main():
    # Set the initial temperature, cooling rate, and number of iterations
    initial_temperature = 100.0
    cooling_rate = 0.95
    iterations = 1000

    # Set an initial solution (starting point)
    initial_solution = random.uniform(-10, 10)

    # Run the simulated annealing algorithm
    final_solution, final_energy = simulated_annealing(initial_solution, initial_temperature, cooling_rate, iterations)

    print(f"Initial Solution: {initial_solution}")
    print(f"Final Solution: {final_solution}")
    print(f"Objective Function Value at Final Solution: {final_energy}")

if __name__ == "__main__":
    main()
