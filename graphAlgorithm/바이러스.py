#바이러스 백준 2606
from collections import deque
n = int(input())
m = int(input())
count = 0
start = 1

graph = [[False] *(n+1) for _ in range(n+1)]
visited = [False] * (n+1)

def bfs(a):
    global count
    q = deque([a])
    visited[a] = True
    while q:
        a = q.popleft()
        for i in range(1, n+1):
            if not visited[i] and graph[a][i]:
                q.append(i)
                visited[i] = True
                count+=1


for i in range(m):
    a,b = list(map(int, input().split()))
    graph[a][b] = True  
    graph[b][a] = True

bfs(start)
print(count)



    
    












