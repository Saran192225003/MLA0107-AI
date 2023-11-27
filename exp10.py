import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))

    def best_first_search(self, start, goal):
        visited = set()
        priority_queue = [(0, start)]
        
        while priority_queue:
            cost, current_node = heapq.heappop(priority_queue)

            if current_node == goal:
                print(f"Goal reached! Total cost: {cost}")
                return

            if current_node not in visited:
                visited.add(current_node)

                for neighbor, edge_cost in self.graph.get(current_node, []):
                    if neighbor not in visited:
                        heapq.heappush(priority_queue, (cost + edge_cost, neighbor))

# Example usage:
if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B', 4)
    g.add_edge('A', 'C', 2)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'E', 3)
    g.add_edge('D', 'E', 1)
    g.add_edge('D', 'F', 7)
    g.add_edge('E', 'G', 2)
    g.add_edge('F', 'G', 6)

    start_node = 'A'
    goal_node = 'G'

    print(f"Best-First Search from {start_node} to {goal_node}:")
    g.best_first_search(start_node, goal_node)
