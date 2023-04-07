import sys
from collections import deque
n,m  = map(int, input().split())
y, x, d = map(int, input().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
#북남서동
direction = [(0,-1),(-1,0),(0,1),(1,0)]

q=deque()
q.append((y,x,d))
graph[y][x] = 2
visited[y][x] == True
def bfs(count):

  while q:
    cy, cx, cd = q.popleft()
    dx, dy = direction[cd]
    nx = cx + dx
    ny = cy + dy
    nd = cd

    if nx < 0 or ny < 0 or nx >= m or ny >= n:
      continue
    #청소하기
    if graph[ny][nx] == 0:
      visited[ny][nx] == True
      graph[ny][nx] = 2
      q.append((ny, nx, nd))
      count += 1
    elif graph[ny][nx] == 1:
      nd = (nd + 1) % 4
      q.append((cy, cx, nd))

  return count

result = bfs(1)
print(result)