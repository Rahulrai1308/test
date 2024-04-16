class Graph:
    def __init__(self, graph, heuristic, start_node):
        self.graph = graph
        self.heuristic = heuristic
        self.start_node = start_node
        self.visited = set()
        self.solution = {}

    def apply_ao_star(self):
        self._ao_star(self.start_node)

    def _ao_star(self, node):
        if node in self.visited:
            return
        
        self.visited.add(node)
        min_cost, min_nodes = self._compute_minimum_cost_child_nodes(node)
        self.heuristic[node] = min_cost
        self.solution[node] = min_nodes
        
        for child in min_nodes:
            self._ao_star(child)

    def _compute_minimum_cost_child_nodes(self, node):
        min_cost = float('inf')
        min_nodes = []

        for option in self.graph.get(node, []):
            cost = sum(self.heuristic[child] + weight for child, weight in option)
            if cost < min_cost:
                min_cost = cost
                min_nodes = [child for child, _ in option]
            elif cost == min_cost:
                min_nodes.extend(child for child, _ in option)

        return min_cost, min_nodes

    def print_solution(self):
        print("Solution Graph:")
        for node, children in self.solution.items():
            print(f"Node: {node}, Children: {children}")


# Example usage
h1 = {'A': 1, 'B': 6, 'C': 2, 'D': 12, 'E': 2, 'F': 1, 'G': 5, 'H': 7, 'I': 7, 'J': 1}
graph1 = {
    'A': [[('B', 1), ('C', 1)], [('D', 1)]],
    'B': [[('G', 1)], [('H', 1)]],
    'C': [[('J', 1)]],
    'D': [[('E', 1), ('F', 1)]],
    'G': [[('I', 1)]]
}

G1 = Graph(graph1, h1, 'A')
G1.apply_ao_star()
G1.print_solution()