import networkx as nx

G = nx.Graph()
edges = [(1, 4), (4, 5), (5, 6)]
G.add_edges_from(edges)

print("Edges added successfully!")