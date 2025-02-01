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

'''_________________________________________________________________________________'''
class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4()) # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()