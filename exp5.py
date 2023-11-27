class State:
    def __init__(self, missionaries, cannibals, boat_position):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat_position = boat_position

    def is_valid(self):
        if self.missionaries < 0 or self.cannibals < 0:
            return False
        if self.missionaries > 3 or self.cannibals > 3:
            return False
        if (
            (self.cannibals > self.missionaries > 0)
            or (3 - self.cannibals > 3 - self.missionaries > 0)
            or (self.boat_position != "left" and self.boat_position != "right")
        ):
            return False
        return True

    def is_goal(self):
        return self.missionaries == 0 and self.cannibals == 0 and self.boat_position == "right"

    def __eq__(self, other):
        return (
            self.missionaries == other.missionaries
            and self.cannibals == other.cannibals
            and self.boat_position == other.boat_position
        )

    def __hash__(self):
        return hash((self.missionaries, self.cannibals, self.boat_position))

def is_valid_move(state, action):
    if action == "MM":
        return State(state.missionaries - 2, state.cannibals, "left").is_valid()
    elif action == "CC":
        return State(state.missionaries, state.cannibals - 2, "left").is_valid()
    elif action == "MC":
        return State(state.missionaries - 1, state.cannibals - 1, "left").is_valid()
    elif action == "M":
        return State(state.missionaries - 1, state.cannibals, "left").is_valid()
    elif action == "C":
        return State(state.missionaries, state.cannibals - 1, "left").is_valid()

def get_valid_moves(state):
    moves = ["MM", "CC", "MC", "M", "C"]
    return [move for move in moves if is_valid_move(state, move)]

def dfs(current_state, path, visited):
    if current_state.is_goal():
        print("Solution found:")
        for step in path:
            print(step)
        return True

    visited.add(current_state)

    for move in get_valid_moves(current_state):
        new_state = apply_move(current_state, move)
        if new_state not in visited and dfs(new_state, path + [move], visited):
            return True

    return False

def apply_move(state, action):
    if action == "MM":
        return State(state.missionaries - 2, state.cannibals, "right")
    elif action == "CC":
        return State(state.missionaries, state.cannibals - 2, "right")
    elif action == "MC":
        return State(state.missionaries - 1, state.cannibals - 1, "right")
    elif action == "M":
        return State(state.missionaries - 1, state.cannibals, "right")
    elif action == "C":
        return State(state.missionaries, state.cannibals - 1, "right")

def solve():
    initial_state = State(3, 3, "left")
    if not dfs(initial_state, [], set()):
        print("No solution found.")

solve()
