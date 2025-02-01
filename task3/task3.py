'''
Завдання 3. Дерева, алгоритм Дейкстри

Розробіть алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі, використовуючи 
бінарну купу. Завдання включає створення графа, використання піраміди для оптимізації вибору вершин 
та обчислення найкоротших шляхів від початкової вершини до всіх інших.

- Програмно реалізовано алгоритм Дейкстри для знаходження найкоротшого шляху у графі з використанням 
бінарної купи (піраміди).
- У межах реалізації завдання створено граф, використано піраміду для оптимізації вибору вершин та 
виконано обчислення найкоротших шляхів від початкової вершини до всіх інших.
'''

from graph_utils import create_graph 
import heapq
import matplotlib.pyplot as plt

def dijkstra_nx(graph, start):
    """Алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі NetworkX"""
    shortest_paths = {node: float('inf') for node in graph.nodes}
    shortest_paths[start] = 0
    priority_queue = [(0, start)]
    previous_nodes = {node: None for node in graph.nodes}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > shortest_paths[current_node]:
            continue

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            distance = current_distance + weight

            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_paths, previous_nodes

def reconstruct_path(previous_nodes, start, end):
    """Відновлення найкоротшого шляху з кінцевої вершини до початкової"""
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous_nodes[current]
    path.reverse()
    return path if path[0] == start else []


def main():
    graph = create_graph()
    start_vertex = 'A'

    # Виконання алгоритму Дейкстри
    shortest_paths, previous_nodes = dijkstra_nx(graph, start_vertex)

    print(f"Найкоротші шляхи від {start_vertex}: {shortest_paths}")

    # Відновлення найкоротшого шляху до конкретної вершини
    target_vertex = 'I'
    path = reconstruct_path(previous_nodes, start_vertex, target_vertex)
    print(f"Найкоротший шлях від {start_vertex} до {target_vertex}: {path}")



if __name__ == "__main__":
    main()