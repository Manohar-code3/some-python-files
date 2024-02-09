# Desing model to color the figure using 3-colors(R,G,B) in such way that each segmant will be colored and no element wil  be arranged to same order
# 1. solve using backtracking
# 2.sove using logical AI that will genrate alram before creating unpreceted solution 
# A->B,D,E;B->A,D,C,F;C->DBEF;E->ADC;D->ABCE;F->BC
def is_safe(graph, node, color, c):
    for neighbor in graph[node]:
        if color[neighbor] == c:
            return False
    return True

def graph_coloring(graph, colors, node, color):
    if node not in graph:
        return True

    for c in colors:
        if is_safe(graph, node, color, c):
            color[node] = c
            unassigned_node = next_unassigned(color, graph)
            if unassigned_node is None:
                return True
            if graph_coloring(graph, colors, unassigned_node, color):
                return True
            color[node] = 0  # Backtrack

    return False

def next_unassigned(color, graph):
    for n in graph:
        if color[n] == 0:
            return n
    return None

# Example graph represented as an adjacency list with nodes A, B, C, D, E, F
graph = {
    'A': ['B', 'D', 'E'],
    'B': ['A', 'C', 'D', 'F'],
    'C': ['D', 'E', 'F'],
    'D': ['A', 'B', 'C', 'E'],
    'E': ['A', 'C', 'D'],
    'F': ['B', 'C'],
}

# Number of colors
num_colors = 3

# Initialize colors with 0 (no color assigned)
node_colors = {node: 0 for node in graph}

if graph_coloring(graph, range(1, num_colors + 1), 'A', node_colors):
    print("Graph coloring solution:")
    for node, color in node_colors.items():
        print(f"Node {node} is colored {['', 'red', 'blue', 'green'][color]}")
else:
    print("No solution found.")
