#1559번
import sys
from collections import deque

def organize():
   for i in range(10,-1,-1):
      for j in range(6):
         if graph[i][j] != '.' and graph[i+1][j] == '.':
            for k in range(i+1,12):
               if k == 11 and graph[k][j] == '.':
                  graph[k][j] = graph[i][j]
               elif graph[k][j] != '.':
                  graph[k-1][j] = graph[i][j]
                  break
            graph[i][j] = '.'
def bfs(i,j,flag):
   cnt = 1
   q = deque()
   direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
   visited = [[False for _ in range(6)] for _ in range(12)]
   q.append([i,j])
   visited[i][j] = True
   while q:
      y, x = q.popleft()
      for di in range(4):
         dy,dx = direction[di]
         nx, ny = x + dx, y + dy
         if ny < 12 and nx < 6 and ny > -1 and nx > -1:
            if graph[ny][nx] == graph[i][j] and not visited[ny][nx]:
               q.append( [ny,nx] )
               visited[ny][nx] = True
               cnt += 1
   #1연쇄 인정
   if cnt >= 4:
      flag += 1
      for i in range(12):
         for j in range(6):
            if visited[i][j]:
               graph[i][j] = '.'

   return flag

graph = [list(map(str,sys.stdin.readline().rstrip())) for _ in range(12)]
color_l = ['.','R','G','B','P','Y']
answer = 0

while True:
   cnt = 0
   for i in range(12):
      for j in range(6):
         if graph[i][j] != '.':
            cnt  = bfs(i,j,cnt)

   if cnt == 0:
      print(answer)
      break
   else:
      answer += 1
   organize()
