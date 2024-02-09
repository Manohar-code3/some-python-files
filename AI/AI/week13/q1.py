# TopologicalSortExample from chatgpt
import networkx as nx
import numpy as np

# Define the adjacency matrix representing the graph
adjacency_matrix = np.array([
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,0,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,0,0,1],
    [0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0]
])

# Create a directed graph from the adjacency matrix
G = nx.DiGraph(adjacency_matrix)

# Perform topological sorting
try:
    topological_order = list(nx.topological_sort(G))
    print("Topological Order:", topological_order)
except nx.NetworkXUnfeasible:
    print("The graph is not a directed acyclic graph (DAG). Topological sorting is not possible.")
