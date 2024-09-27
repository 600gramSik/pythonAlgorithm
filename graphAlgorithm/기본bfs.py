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

def BFS(graph, start_node):
    visited = list() #방문한 노드를 담을 배열
    queue = list() #방문 예정인 노드를 담을 배열
    
    queue.append(start_node)
    
    while queue:
        node = queue.pop(0)

        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    
    print("bfs-", visited)
    return visited

BFS(myGraph, 'A')
