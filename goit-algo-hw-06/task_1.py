import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

cities = [
    "Kyiv",
    "Lviv",
    "Kharkiv",
    "Dnipro",
    "Odesa",
    "Vinnytsia",
    "Poltava"
]
G.add_nodes_from(cities)

roads = [
    ("Kyiv", "Lviv"),
    ("Kyiv", "Vinnytsia"),
    ("Kyiv", "Poltava"),
    ("Poltava", "Kharkiv"),
    ("Kyiv", "Dnipro"),
    ("Dnipro", "Odesa"),
]
G.add_edges_from(roads)

print("Кількість вершин:", G.number_of_nodes())
print("Кількість ребер:", G.number_of_edges())

print("\nСтупінь вершин:")
for city, degree in G.degree():
    print(f"{city}: {degree}")

plt.figure(figsize=(9, 6))
pos = nx.spring_layout(G, seed=42)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=1200,
    font_size=10,
    width=2
)

plt.title("Транспортна мережа міст України")
plt.show()
