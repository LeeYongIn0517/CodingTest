#1743번
import sys
from collections import deque

n,m,k = map(int,sys.stdin.readline().split())
tile = [[0]*m for _ in range(n)]
visited = [[False]*m for _ in range(n)]
answer = 0
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for _ in range(k):
    y,x = map(int,sys.stdin.readline().split())
    tile[y-1][x-1] = 1

def bfs(x,y):
   global size
   q.append((x,y))
   while q:
      i, j =  q.popleft()
      for d in range(4):
         ni, nj = dy[d] + i, dx[d] + j
         if ni >= 0 and nj >= 0 and ni < n and nj < m:
            if tile[ni][nj] == 1 and not visited[ni][nj]:
               size += 1
               q.append((ni,nj))
               visited[ni][nj] = True

q=deque()
for i in range(n):
    for j in range(m):
        if not visited[i][j] and tile[i][j] == 1 :
            size = 0
            bfs(i,j)
            visited[i][j] = True
            answer = max(answer, size)

print(answer)