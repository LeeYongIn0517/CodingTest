#7576번
from collections import deque
n,m = map(int,input().split())
box = [list( map(int, input().split()) ) for _ in range(m)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
q = deque()
for i in range(m):
   for j in range(n):
      if box[i][j] == 1:
         q.append((i, j))

def bfs():
   while q:
      y,x = q.popleft()

      for i in range(4):
         ny,nx = y+dy[i], x+dx[i]
         if 0<=ny<m and 0<=nx<n and box[ny][nx] == 0:
            q.append((ny,nx))
            box[ny][nx] = box[y][x] + 1

bfs()

res = 0
for i in range(m):
   for j in range(n):
      if box[i][j] == 0:
         print(-1)
         exit(0)
   res = max(res, max(box[i]))
print(res - 1)
