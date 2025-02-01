'''
Завдання 4. Візуалізація піраміди

Наступний код виконує побудову бінарних дерев. Виконайте аналіз коду, щоб зрозуміти, як він працює.
Використовуючи як базу цей код, побудуйте функцію, що буде візуалізувати бінарну купу.
 👉🏻 Примітка. Суть завдання полягає у створенні дерева із купи.
'''

import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt

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

def tree_to_list(root):
    """Converts a binary tree to a list using level-order traversal."""
    if not root:
        return []

    tree_list = []
    queue = [(root, 0)]

    while queue:
        node, level = queue.pop(0)
        tree_list.append(node.val)

        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))

    return tree_list


def list_to_heap(tree_list):
    """Transforms the list representation into a binary heap (min-heap)."""
    heapq.heapify(tree_list)
    return tree_list

def heap_to_tree(heap_list):
    """Converts a heap represented as a list back to a binary tree."""
    if not heap_list:
        return None

    root = Node(heap_list[0])
    nodes = [root]
    i = 1

    while i < len(heap_list):
        current = nodes.pop(0)  # Use pop(0) to maintain FIFO order for level-order

        if i < len(heap_list):
            current.left = Node(heap_list[i])
            nodes.append(current.left)
            i += 1

        if i < len(heap_list):
            current.right = Node(heap_list[i])
            nodes.append(current.right)
            i += 1

    return root


def tree_to_heap_to_tree(tree_root):
    # перетворення дерева на купу (використовується перетворення спочатку дерева на список)
    return heap_to_tree(list_to_heap(tree_to_list(tree_root)))


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def main():
    # Створення дерева
    root = Node(2)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)
    root.right.right = Node(7)

    # Відображення дерева отриманого з купи 
    draw_tree(tree_to_heap_to_tree(root))

if __name__ == '__main__':
        main()