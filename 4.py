from collections import defaultdict

def bfs(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)

    while queue:
        node = queue.pop(0)
        print(node, end=' ')

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=' ')

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Taking user input for the graph
graph = defaultdict(list)
num_edges = int(input("Enter the number of edges: "))
for _  in range(num_edges):
    src, dest = input("Enter edge (source destination): ").split()
    graph[src].append(dest)
    graph[dest].append(src)

print(graph)
start_node = input("Enter the starting node: ")

print("BFS Traversal:")
bfs(graph, start_node)
print("\nDFS Traversal:")
dfs(graph, start_node)
