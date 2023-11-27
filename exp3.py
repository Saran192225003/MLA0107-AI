from collections import deque

def water_jug_problem(capacity_jug4, capacity_jug3, target):
    visited_states = set()
    initial_state = (0, 0)  # Initial state (0 gallons in jug4, 0 gallons in jug3)
    queue = deque([initial_state])

    while queue:
        current_state = queue.popleft()

        if current_state == (target, 0):
            # Solution found
            print("Solution found!")
            print_path(current_state)
            return

        visited_states.add(current_state)

        # Fill jug4
        fill_jug4 = (capacity_jug4, current_state[1])
        if fill_jug4 not in visited_states and fill_jug4 not in queue:
            queue.append(fill_jug4)

        # Fill jug3
        fill_jug3 = (current_state[0], capacity_jug3)
        if fill_jug3 not in visited_states and fill_jug3 not in queue:
            queue.append(fill_jug3)

        # Pour water from jug4 to jug3
        pour_jug4_to_jug3 = (
            max(0, current_state[0] - (capacity_jug3 - current_state[1])),
            min(capacity_jug3, current_state[0] + current_state[1]),
        )
        if pour_jug4_to_jug3 not in visited_states and pour_jug4_to_jug3 not in queue:
            queue.append(pour_jug4_to_jug3)

        # Pour water from jug3 to jug4
        pour_jug3_to_jug4 = (
            min(capacity_jug4, current_state[0] + current_state[1]),
            max(0, current_state[1] - (capacity_jug4 - current_state[0])),
        )
        if pour_jug3_to_jug4 not in visited_states and pour_jug3_to_jug4 not in queue:
            queue.append(pour_jug3_to_jug4)

        # Empty jug4
        empty_jug4 = (0, current_state[1])
        if empty_jug4 not in visited_states and empty_jug4 not in queue:
            queue.append(empty_jug4)

        # Empty jug3
        empty_jug3 = (current_state[0], 0)
        if empty_jug3 not in visited_states and empty_jug3 not in queue:
            queue.append(empty_jug3)

    print("No solution found.")

def print_path(final_state):
    path = []
    while final_state != (0, 0):
        path.append(final_state)
        final_state = get_previous_state(final_state)

    path.append((0, 0))
    path.reverse()

    for state in path:
        print(f"Jug4: {state[0]} gallons, Jug3: {state[1]} gallons")

def get_previous_state(current_state):
    if current_state[0] == 0:
        return (0, current_state[1] - 1)
    elif current_state[1] == 0:
        return (current_state[0] - 1, 0)
    else:
        return (current_state[0] - 1, current_state[1] + 1)

if __name__ == "__main__":
    water_jug_problem(4, 3, 2)
