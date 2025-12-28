from collections import deque


def bfs_iterative(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        vertex, path = queue.popleft()

        if vertex == goal:
            return path

        if vertex not in visited:
            visited.add(vertex)

            for neighbor in graph[vertex]:
                queue.append((neighbor, path + [neighbor]))

    return None


def dfs_iterative(graph, start, goal):
    stack = [(start, [start])]
    visited = set()

    while stack:
        vertex, path = stack.pop()

        if vertex == goal:
            return path

        if vertex not in visited:
            visited.add(vertex)

            for neighbor in graph[vertex]:
                stack.append((neighbor, path + [neighbor]))

    return None

graph = {
    "Kyiv": ["Lviv", "Vinnytsia", "Poltava", "Odesa"],
    "Lviv": ["Kyiv", "Vinnytsia"],
    "Vinnytsia": ["Kyiv", "Lviv", "Dnipro"],
    "Poltava": ["Kyiv", "Kharkiv"],
    "Kharkiv": ["Poltava", "Dnipro"],
    "Dnipro": ["Odesa", "Kharkiv", "Vinnytsia"],
    "Odesa": ["Dnipro", "Kyiv"]
}

bfs_path = bfs_iterative(graph, "Lviv", "Odesa")
print("BFS path:", bfs_path)

dfs_path = dfs_iterative(graph, "Lviv", "Odesa")
print("DFS path:", dfs_path)


