import time
import uuid
from collections import deque

import matplotlib.pyplot as plt
import networkx as nx


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.color = "#B0B0B0"
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is None:
        return

    graph.add_node(node.id, color=node.color, label=node.val)

    if node.left:
        graph.add_edge(node.id, node.left.id)
        l = x - 1 / 2 ** layer
        pos[node.left.id] = (l, y - 1)
        add_edges(graph, node.left, pos, l, y - 1, layer + 1)

    if node.right:
        graph.add_edge(node.id, node.right.id)
        r = x + 1 / 2 ** layer
        pos[node.right.id] = (r, y - 1)
        add_edges(graph, node.right, pos, r, y - 1, layer + 1)


def draw_tree(root, title):
    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    add_edges(tree, root, pos)

    colors = [n[1]['color'] for n in tree.nodes(data=True)]
    labels = {n[0]: n[1]['label'] for n in tree.nodes(data=True)}

    plt.clf()
    plt.title(title)
    nx.draw(tree, pos, labels=labels,
            node_color=colors, node_size=2500, arrows=False)
    plt.pause(1)


def dfs_visual(root):
    stack = [root]

    while stack:
        node = stack.pop()

        node.color = "#FF0000"
        draw_tree(root, "DFS (обхід у глибину)")

        node.color = "#1F77B4"

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


def bfs_visual(root):
    queue = deque([root])

    while queue:
        node = queue.popleft()

        node.color = "#FF0000"
        draw_tree(root, "BFS (обхід у ширину)")

        node.color = "#1F77B4"

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


root = Node(0)
root.left = Node(4)
root.right = Node(1)
root.left.left = Node(5)
root.left.right = Node(10)
root.right.left = Node(3)

plt.figure(figsize=(8, 5))

dfs_visual(root)
time.sleep(2)

for n in [root, root.left, root.right,
          root.left.left, root.left.right, root.right.left]:
    n.color = "#B0B0B0"

bfs_visual(root)

plt.show()
