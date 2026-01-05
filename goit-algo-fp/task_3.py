import heapq


def print_table(distances, visited):
    print("{:<10} {:<10} {:<10}".format("Вершина", "Відстань", "Перевірено"))
    print("-" * 30)

    for vertex in distances:
        distance = distances[vertex]
        if distance == float('inf'):
            distance = "∞"
        else:
            distance = str(distance)

        status = "Так" if vertex in visited else "Ні"
        print("{:<10} {:<10} {:<10}".format(vertex, distance, status))
    print()


def dijkstra(graph, start):
    distances = {v: float('inf') for v in graph}
    distances[start] = 0

    visited = []
    heap = [(0, start)]

    while heap:
        current_dist, current_vertex = heapq.heappop(heap)
        if current_vertex in visited:
            continue
        visited.append(current_vertex)
        for neighbor, weight in graph[current_vertex].items():
            new_dist = current_dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
        print_table(distances, visited)
    return distances


graph = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'D': 3},
    'C': {'A': 10, 'D': 2},
    'D': {'B': 3, 'C': 2, 'E': 4},
    'E': {'D': 4}
}

dijkstra(graph, 'A')
