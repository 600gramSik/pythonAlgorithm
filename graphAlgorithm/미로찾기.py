#백준 미로찾기 2178번
from collections import deque
n,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def BFS(x,y):
    #상하좌우 방향 정의
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    #시작점을 queue에 삽입
    queue.append((x,y))

    while queue:
        #현재 좌표를 큐에서 꺼낸다
        x, y =queue.popleft()
        #현재 위치에서 상, 하, 좌, 우로 이동 가능한지 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))
    return graph[n-1][m-1]

print(BFS(0,0))





