def is_valid_coloring(graph, coloring):
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            if coloring[node] == coloring[neighbor]:
                return False
    return True

def is_valid_partial_coloring(graph, coloring, node):
    for neighbor in graph[node]:
        if neighbor in coloring and coloring[node] == coloring[neighbor]:
            return False
    return True

def generate_initial_solution(graph, colors):
    node_colors = {}
    for node in graph:
        available_colors = set(colors)
        for neighbor in graph[node]:
            if neighbor in node_colors and node_colors[neighbor] in available_colors:
                available_colors.remove(node_colors[neighbor])
        if not available_colors:
            return None  # No solution is possible
        node_colors[node] = available_colors.pop()
    return node_colors

def graph_coloring_with_alarms(graph, colors):
    initial_solution = generate_initial_solution(graph, colors)
    
    if initial_solution is None:
        print("No solution is possible. Alarm raised.")
        return None
    
    for node in graph:
        if not is_valid_partial_coloring(graph, initial_solution, node):
            print(f"Alarm: Invalid partial coloring at node {node}")
    
    if is_valid_coloring(graph, initial_solution):
        print("Valid graph coloring solution:")
        for node, color in initial_solution.items():
            print(f"Node {node} is colored {['', 'red', 'blue', 'green'][color]}")
        return initial_solution
    else:
        print("Invalid solution. Alarm raised.")
        return None

# Given graph represented as an adjacency list with nodes A, B, C, D, E, F
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

# Solve the graph coloring CSP with alarms
solution = graph_coloring_with_alarms(graph, range(1, num_colors + 1))

if solution:
    # You can use 'solution' for further processing if needed
    pass
