from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = defaultdict(list)
        self.weights = {}

    def add_edge(self, u, v, w):
        # Add an edge to the graph with weight w
        self.edges[u].append(v)
        self.weights[(u, v)] = w

def shortest_path(graph, source, destination):
    # Initialize the distance and parent arrays
    distance = [float("inf")] * graph.vertices
    distance[source] = 0
    parent = [-1] * graph.vertices

    # Perform dynamic programming to find shortest paths
    for i in range(source, graph.vertices):
        for j in graph.edges[i]:
            if distance[j] > distance[i] + graph.weights[(i, j)]:
                distance[j] = distance[i] + graph.weights[(i, j)]
                parent[j] = i

    # Build the shortest path by traversing the parent array
    path = []
    node = destination
    while node != source:
        path.append(node)
        node = parent[node]
    path.append(source)
    path.reverse()

    # Return the shortest path and shortest distance
    return path, distance[destination]

# Example usage
g = Graph(8)
g.add_edge(0, 1, 1)
g.add_edge(0, 2, 2)
g.add_edge(1, 3, 3)
g.add_edge(1, 4, 2)
g.add_edge(2, 3, 1)
g.add_edge(2, 4, 3)
g.add_edge(3, 5, 1)
g.add_edge(4, 5, 2)
g.add_edge(5, 6, 1)
g.add_edge(6, 7, 1)

# Find the shortest path from node 0 to node 7 and print the results
path, distance = shortest_path(g, 0, 7)
print("Shortest path:", path)
print("Shortest distance from source to destination:", distance)

