#2667번
from collections import deque
n = int(input())
graph = [list(input()) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
count_arr = []
count = 0
q = deque()
si,sj = 0,0
flag = False
direction = [(1,0),(-1,0),(0,1),(0,-1)]

go_on_flag = True

while go_on_flag:
   go_on_flag = False

   for i,lv in enumerate(graph):
      for j,v in enumerate(lv):
         if(v == '1' and visited[i][j] == False):
            si,sj = i,j
            flag = True
            go_on_flag = True
            break
      if flag:
         break

   if not go_on_flag:
      break

   q.append((si,sj))
   visited[si][sj] = True
   count += 1
   while q:
      ti,tj = q.popleft()
      for i,v in enumerate(direction):
         y,x = v
         ni,nj = ti+y, tj+x
         if(ni >= 0 and ni < n and nj >= 0 and nj < n):
            if(graph[ni][nj] == '1' and visited[ni][nj]==False):
               q.append((ni,nj))
               visited[ni][nj] = True
               count += 1
   if flag:
      count_arr.append(count)
   flag,count = False,0 #초기화


print(len(count_arr))
count_arr.sort()
for i,v in enumerate(count_arr):
   print(v)