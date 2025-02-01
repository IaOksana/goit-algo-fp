'''
Завдання 5. Візуалізація обходу бінарного дерева

Використовуючи код із завдання 4 для побудови бінарного дерева, необхідно створити програму на Python, 
яка візуалізує обходи дерева: у глибину та в ширину.

Вона повинна відображати кожен крок у вузлах з різними кольорами, використовуючи 16-систему RGB 
(приклад #1296F0). Кольори вузлів мають змінюватися від темних до світлих відтінків, залежно від 
послідовності обходу. Кожен вузол при його відвідуванні має отримувати унікальний колір, який 
візуально відображає порядок обходу.

👉🏻 Примітка. Використовуйте стек та чергу, НЕ рекурсію
'''


import uuid
import matplotlib.colors as mcolors
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt
from time import sleep
from matplotlib.animation import FuncAnimation
from graph_utils import Node, draw_tree, add_edges

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


def dfs_iterative(graph, start_vertex):
    path = []
    visited = set()
    # Використовуємо стек для зберігання вершин
    stack = [start_vertex]  
    while stack:
        # Вилучаємо вершину зі стеку
        vertex = stack.pop()  
        if vertex not in visited:
            print(vertex, end=' ')
            # Відвідуємо вершину
            visited.add(vertex)
            path.append(vertex)
            # Додаємо сусідні вершини до стеку
            stack.extend(reversed(list(graph.neighbors(vertex))))  
    
    return path



def bfs_iterative(graph, start):
    # Ініціалізація порожньої множини для зберігання відвіданих вершин
    visited = set()
    path = []
    # Ініціалізація черги з початковою вершиною
    queue = deque([start])

    while queue:  # Поки черга не порожня, продовжуємо обхід
        # Вилучаємо першу вершину з черги
        vertex = queue.popleft()
        # Перевіряємо, чи була вершина відвідана раніше
        if vertex not in visited:
            # Якщо не була відвідана, друкуємо її
            print(vertex, end=" ")
            # Додаємо вершину до множини відвіданих вершин
            visited.add(vertex)
            path.append(vertex)
            # Додаємо всіх невідвіданих сусідів вершини до кінця черги
            # Операція різниці множин вилучає вже відвідані вершини зі списку сусідів
            queue.extend(set(list(graph.neighbors(vertex))) - visited)
    # Повертаємо множину відвіданих вершин після завершення обходу
    return path  

def adjust_brightness(hex_color, factor=0.8):
    # Змінює яскравість кольору (від світлого до темного). factor < 1 — затемнення, factor > 1 — освітлення

    rgb = mcolors.hex2color(hex_color)  # Конвертуємо HEX у RGB (0-1)
    darker_rgb = tuple(max(0, min(1, c * factor)) for c in rgb)  # Затемнюємо
    return mcolors.to_hex(darker_rgb)  # Конвертуємо назад у HEX

def draw_tree(tree_root, traversal_type = True):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    fig, ax = plt.subplots()
    path = []

    def update(frame):
        sleep(0.5)
        print("update")
        ax.clear()
        
        if len(path) != 0:
            nodes = path[:frame + 1]
            nx.draw(tree, pos=pos, labels=labels, node_size=2000, node_color=colors, ax=ax, font_weight='bold')
            if not traversal_type:
                nx.draw_networkx_nodes(tree, pos=pos, nodelist=nodes, node_color='orange', node_size=2000, ax=ax)
            ax.set_title(f'Press Enter to change mode.   { "BFS" if not traversal_type else "DFS"} ')
        else:   
            ax.set_title(f'Press Enter to start')
            nx.draw(tree, pos=pos, labels=labels, node_size=2000, node_color='lightblue', ax=ax, font_weight='bold')

    def on_key_press(event):
        nonlocal traversal_type  # Access and modify the outer scope's traversal_type
        nonlocal ani # Access the animation object to stop and restart it
        nonlocal path # same as above
        nonlocal colors

        if event.key == 'enter':
            if traversal_type:
                traversal_type = False
                path = bfs_iterative(tree, tree_root.id)
                colors = [node[1].get('color', 'lightblue') for node in tree.nodes(data=True)]
            else:
                traversal_type = True
                path = dfs_iterative(tree, tree_root.id)
                colors = [adjust_brightness('#42F6F9', i*0.2)  for i in range(len(tree.nodes(data=True))) ]

            ani.event_source.stop()  # Stop the current animation

            ani._func = update
            ani.frames = len(path) # define new frames number
            ani.event_source.start()


    #path = dfs_iterative(tree, tree_root.id)       
    colors = [node[1].get('color', 'lightblue') for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    
    nx.draw(tree, pos=pos, labels=labels, node_size=2000, node_color='lightblue', ax=ax, font_weight='bold')
   
    ani = FuncAnimation(fig, update, frames=len(list(tree.nodes)), repeat=True)
    fig.canvas.mpl_connect('key_press_event', on_key_press)
    plt.show()
    


# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Відображення дерева
draw_tree(root)
