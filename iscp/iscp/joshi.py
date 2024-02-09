import sys

def shortestPath(n, edges, visitNodes):
    # Create an adjacency list to represent the tree
    graph = {}
    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)

    # Initialize variables to keep track of visited nodes and distances
    visited = set()
    distances = [sys.maxsize] * (n + 1)

    # Start the DFS from node 1
    def dfs(node):
        visited.add(node)

        # Check if all visitNodes are visited
        all_visited = all(node in visited for node in visitNodes)

        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
                distances[node] = min(distances[node], distances[neighbor] + 1)

        # If all visitNodes are visited, calculate the distance to node n
        if all_visited:
            distances[n] = min(distances[n], distances[node] + 1)

    dfs(1)
    
    # Check if all visitNodes are visited, if not, return -1
    if not all(node in visited for node in visitNodes):
        return -1

    # Return the shortest path from 1 to n
    return distances[n] if distances[n] != sys.maxsize else -1

# Example usage
n = 5
edges = [[1, 2], [1, 3], [3, 4], [3, 5]]
visitNodes = [2, 4]
result = shortestPath(n, edges, visitNodes)
print(result)  # Output: 3