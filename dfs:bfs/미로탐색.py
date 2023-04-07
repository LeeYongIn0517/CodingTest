#백준 2178번
from collections import deque

n,m = map(int, input().split())
graph = []
#상하좌우
dx = [0,0,-1,1]
dy = [-1,1,0,0]

for i in range(n):
  graph.append(list(map(int, input())))

q = deque()
q.append((0,0))

while q:
  cx, cy = q.popleft()
  for i in range(4):
    nx = cx + dx[i]
    ny = cy + dy[i]
    if (nx >= m or ny >= n or nx < 0 or ny < 0):
      continue
    if nx >= 0 and ny >= 0 and nx < m and ny < n and graph[ny][nx] == 1:
      q.append((nx, ny))
      graph[ny][nx] = graph[cy][cx] + 1

print(graph[n-1][m-1])