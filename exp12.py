class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, node1, node2):
        self.add_node(node1)
        self.add_node(node2)
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    def color_map(self):
        colors = {}
        for node in self.graph:
            neighbor_colors = {colors[neighbor] for neighbor in self.graph[node] if neighbor in colors}
            available_colors = {1, 2, 3} - neighbor_colors
            if available_colors:
                colors[node] = min(available_colors)
            else:
              
                colors[node] = max(colors.values()) + 1

        return colors

def main():
  
    map_graph = Graph()
    map_graph.add_edge("A", "B")
    map_graph.add_edge("A", "C")
    map_graph.add_edge("B", "C")
    map_graph.add_edge("B", "D")
    map_graph.add_edge("C", "D")

    coloring = map_graph.color_map()
    print("Region colors:", coloring)

if __name__ == "__main__":
    main()
