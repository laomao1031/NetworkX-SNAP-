import time
import networkx as nx

G = nx.read_edgelist("facebook_combined.txt", nodetype=int)

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
avg_degree = sum(dict(G.degree()).values()) / num_nodes

bfs_start = time.perf_counter()
for _ in range(100):
    list(nx.bfs_edges(G, source=0))
bfs_time = (time.perf_counter() - bfs_start) / 100

dfs_start = time.perf_counter()
for _ in range(100):
    list(nx.dfs_edges(G, source=0))
dfs_time = (time.perf_counter() - dfs_start) / 100

print(f"Nodes |V|: {num_nodes}")
print(f"Edges |E|: {num_edges}")
print(f"Average Degree: {avg_degree:.2f}")
print(f"BFS Average Time: {bfs_time:.6f} seconds")
print(f"DFS Average Time: {dfs_time:.6f} seconds")
print(f"Time Difference (DFS - BFS): {dfs_time - bfs_time:.6f} seconds")