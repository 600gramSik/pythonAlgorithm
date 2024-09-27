myGraph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['A', 'H'],
    'E': ['B', 'I'],
    'F': ['C', 'J'],
    'G': ['C'],
    'H': ['D'],
    'I': ['E'],
    'J': ['F']
}

def DFS(graph, start_node):
    visited = list()
    stack = list()

    stack.append(start_node)
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph[node]))
    
    print("dfs-", visited)
    return visited

DFS(myGraph, 'A')

