import random

def hill_climbing(objective_function, initial_state, max_iterations=1000):
    current_state = initial_state
    current_value = objective_function(current_state)

    for _ in range(max_iterations):
        neighbors = generate_neighbors(current_state)
        next_state = get_best_neighbor(neighbors, objective_function)
        next_value = objective_function(next_state)

        if next_value > current_value:
            current_state = next_state
            current_value = next_value

    return current_state, current_value

def generate_neighbors(state):
    neighbors = []
    for i in range(len(state)):
        neighbor = list(state)
        neighbor[i] += random.uniform(-1, 1)
        neighbors.append(tuple(neighbor))
    return neighbors

def get_best_neighbor(neighbors, objective_function):
    return max(neighbors, key=objective_function)

def objective_function(x):
    return -x**2

initial_state = (0.0,)

final_state, final_value = hill_climbing(objective_function, initial_state)

print("Initial State:", initial_state)
print("Final State:", final_state)
print("Final Value:", final_value)
