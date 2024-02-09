def generate_alarm(graph):
    # Define a list of allowed edges based on the given graph
    allowed_edges = set()
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            allowed_edges.add((node, neighbor))

    # Check for unexpected or unprecedented edges in the graph
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            if (neighbor, node) not in allowed_edges:
                alarm_message = f"Unexpected edge detected: ({node}, {neighbor})"
                return alarm_message

    # If no unexpected edges were found, return a message indicating no alarm
    return "No alarm: The graph is consistent with the provided structure."

# Example usage with the given graph
graph = {
    'A': ['B', 'D', 'E'],
    'B': ['A', 'C', 'D', 'F'],
    'C': ['D', 'E', 'F'],
    'D': ['A', 'B', 'C', 'E'],
    'E': ['A', 'C', 'D'],
    'F': ['B', 'C'],
}

alarm_message = generate_alarm(graph)
print(alarm_message)
