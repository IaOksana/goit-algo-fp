'''
Завдання 3. Дерева, алгоритм Дейкстри

Розробіть алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі, використовуючи 
бінарну купу. Завдання включає створення графа, використання піраміди для оптимізації вибору вершин 
та обчислення найкоротших шляхів від початкової вершини до всіх інших.
'''

# Task 3
# Implement Dijkstra's algorithm to find the shortest path in the developed graph: add weights to 
# the edges and find the shortest path between all graph vertices.
# - Add weights to the graph, and implement the Dijkstra algorithm to find the shortest path in the 
# developed graph.

from graph_utils import create_graph

def dijkstra(graph, start_node):
    """Finds the shortest paths from a start node to all other nodes using Dijkstra's algorithm."""
    distances = {node: float('inf') for node in graph.nodes}
    distances[start_node] = 0
    predecessors = {node: None for node in graph.nodes}
    visited = set()

    while len(visited) < len(graph.nodes):
        current_node = min((node for node in graph.nodes if node not in visited), key=lambda node: distances[node])
        visited.add(current_node)

        for neighbor in graph.neighbors(current_node):
            distance = distances[current_node] + graph.edges[current_node, neighbor]['weight']
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
    
    paths = {}
    for node in graph.nodes:
        path = []
        current = node
        while current is not None:
            path.insert(0, current)
            current = predecessors[current]
        paths[node] = path

    return distances, paths


def main():

    # Create the graph
    graph = create_graph()

    # Find shortest paths from node 'A' to all other nodes
    shortest_distances, shortest_paths  = dijkstra(graph, 'A')

    print("Shortest paths from node 'A':")
    for node, distance in shortest_distances.items():
        print(f"  To node '{node}' distance is {distance} via {shortest_paths[node]}")


if __name__ == "__main__":
    main()