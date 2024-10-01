#바이러스 백준 2606
from collections import deque
n = int(input())
m = int(input())
count = 0
start = 1

graph = [[False] *(n+1) for _ in range(n+1)]
visited = [False] * (n+1)

def bfs(v):
    global count  # 전역 변수 count 사용
    q = deque([v])  # 시작 노드 v를 큐에 넣고 BFS 시작
    visited[v] = True  # 시작 노드를 방문 처리
    while q:  # 큐가 빌 때까지 반복
        v = q.popleft()  # 큐에서 첫 번째 노드를 꺼냄
        for i in range(1, n+1):  # 1번부터 n번까지의 노드를 확인
            if not visited[i] and graph[v][i]:  # 노드 i가 방문되지 않았고, v와 연결되어 있으면
                q.append(i)  # 큐에 노드 i를 추가
                visited[i] = True  # 노드 i를 방문했다고 표시
                count += 1  # 방문한 노드의 개수를 증가


for i in range(m):
    a,b = list(map(int, input().split()))
    graph[a][b] = True  
    graph[b][a] = True

bfs(start)
print(count)



    
    












