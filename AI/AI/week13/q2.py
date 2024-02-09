# lab java code into python
from collections import defaultdict

def topological_sort(adjacency_matrix, vertices_to_consider):
    vertices = len(adjacency_matrix)
    stack = []
    visited = [False] * vertices

    def topological_sort_util(vertex):
        visited[vertex] = True
        for neighbor in range(vertices):
            if adjacency_matrix[vertex][neighbor] == 1 and not visited[neighbor]:
                topological_sort_util(neighbor)
        stack.append(vertex)

    for vertex in vertices_to_consider:
        if not visited[vertex]:
            topological_sort_util(vertex)

    print("Topological Sorting for specified vertices:")
    while stack:
        print(stack.pop(), end=" ")

# Create an adjacency matrix for the graph
adjacency_matrix = [
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,0,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,0,0,1],
    [0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,1,0,0,0,0,0,0,1,1,0]
]

# Vertices to consider in the topological sorting
vertices_to_consider = [2, 3, 5, 7, 8, 9, 10, 11]

# Perform topological sort for the specified vertices
topological_sort(adjacency_matrix, vertices_to_consider)
# and its worked.
