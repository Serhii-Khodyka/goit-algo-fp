import uuid
import heapq

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
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


def draw_tree(tree_root, colors=None):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    if colors is None:
        colors = [node[1]['color'] for node in tree.nodes(data=True)]
    else:
        colors = [colors[node[0]] for node in tree.nodes(data=True)]

    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def build_heap_tree(heap, index=0):
    if index < len(heap):
        node = Node(heap[index])
        node.left = build_heap_tree(heap, 2 * index + 1)
        node.right = build_heap_tree(heap, 2 * index + 2)
        return node
    return None

def generate_color(step, total_steps):
    base_color = [130, 130, 15]
    lighten_factor = 255 * step // total_steps
    new_color = [min(255, base_color[i] + lighten_factor) for i in range(3)]
    return f'#{new_color[0]:02x}{new_color[1]:02x}{new_color[2]:02x}'


def dfs_visualize(root, total_steps):
    visited = set()
    stack = [(root, 0)]
    colors = {}
    step = 0

    while stack:
        node, depth = stack.pop()
        if node and node.id not in visited:
            visited.add(node.id)
            colors[node.id] = generate_color(step, total_steps)
            step += 1

            stack.append((node.right, depth + 1))
            stack.append((node.left, depth + 1))

    return colors


def bfs_visualize(root, total_steps=1):
    visited = set()
    queue = [(root, 0)]
    colors = {}
    step = 0

    while queue:
        node, depth = queue.pop(0)
        if node and node.id not in visited:
            visited.add(node.id)
            colors[node.id] = generate_color(step, total_steps)
            step += 1

            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))

    return colors

def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

if __name__ == '__main__':
    heap_list = [1, 3, 5, 7, 9, 2, 4, 34, 2, 1, 2]
    heapq.heapify(heap_list)
    # Побудова дерева з купи
    heap_tree_root = build_heap_tree(heap_list)

    # Обрахунок кількості кроків (вузлів)
    total_steps = count_nodes(heap_tree_root)

    # DFS візуалізація
    dfs_colors = dfs_visualize(heap_tree_root, total_steps)
    draw_tree(heap_tree_root, dfs_colors)

    # BFS візуалізація
    bfs_colors = bfs_visualize(heap_tree_root, total_steps)
    draw_tree(heap_tree_root, bfs_colors)