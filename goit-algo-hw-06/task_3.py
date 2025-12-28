def print_table(distances, visited):
    print("{:<10} {:<10} {:<10}".format("Вершина", "Відстань", "Перевірено"))
    print("-" * 30)

    for vertex in distances:
        distance = distances[vertex]
        if distance == float('infinity'):
            distance = "∞"
        else:
            distance = str(distance)

        status = "Так" if vertex in visited else "Ні"
        print("{:<10} {:<10} {:<10}".format(vertex, distance, status))
    print("\n")


def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    unvisited = list(graph.keys())
    visited = []

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        print(f"Current vertex: {current_vertex}")

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        visited.append(current_vertex)
        unvisited.remove(current_vertex)

        print_table(distances, visited)

    return distances


graph = {
    "Kyiv": {
        "Lviv": 540,
        "Vinnytsia": 270,
        "Poltava": 350,
        "Odesa": 475
    },
    "Lviv": {
        "Kyiv": 540,
        "Vinnytsia": 360
    },
    "Vinnytsia": {
        "Kyiv": 270,
        "Lviv": 360,
        "Dnipro": 600
    },
    "Poltava": {
        "Kyiv": 350,
        "Kharkiv": 150
    },
    "Kharkiv": {
        "Poltava": 150,
        "Dnipro": 215
    },
    "Dnipro": {
        "Vinnytsia": 600,
        "Kharkiv": 215,
        "Odesa": 470
    },
    "Odesa": {
        "Dnipro": 470,
        "Kyiv": 475
    }
}

distances = dijkstra(graph, "Lviv")

print("\nFinal distances from Lviv:")
for city, dist in distances.items():
    print(f"{city}: {dist}")
