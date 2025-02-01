import networkx as nx
import uuid
import matplotlib.pyplot as plt

# # Define the nodes (people in the social network)
# nodes = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank']

# # Define the edges (connections between people)
# edges = [('Alice', 'Bob'), ('Alice', 'Charlie'), ('Bob', 'Charlie'),
#         ('Bob', 'David'), ('Charlie', 'Eve'), ('David', 'Eve'),
#         ('Eve', 'Frank')]

nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'),
        ('C', 'F'), ('C', 'G'), ('D', 'H'), ('E', 'I'),
        ('F', 'I'), ('G', 'I'), ('G', 'B')]

weights = {
    ('A', 'B'): 4,
    ('A', 'C'): 1,
    ('B', 'D'): 1,
    ('B', 'E'): 3,
    ('C', 'F'): 1,
    ('C', 'G'): 2,
    ('D', 'H'): 2,
    ('E', 'I'): 6,
    ('F', 'I'): 4,
    ('G', 'I'): 4,
    ('G', 'B'): 2,
}



def create_graph():
    # Create the graph
    graph = nx.Graph()
    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)

    for edge, weight in weights.items():
        graph.edges[edge]['weight'] = weight

    return graph