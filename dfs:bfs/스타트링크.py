#5041번
from collections import deque
f,s,g,u,d = map(int, input().split())
graph = [[] for _ in range(f+1)]
visited = [False for _ in range(f+1)]
count, answerFound = 0, False
q=deque()

for i in range(1,f+1):
   if i+u <= f:
      graph[i].append(i+u)
   if i-d >= 1:
    graph[i].append(i-d)

q.append((s,0))
visited[s] = True
while q:
   t,c = q.popleft()
   l = graph[t]
   if t == g:
      count = c
      answerFound = True
   for i,v in enumerate(l):
      if not visited[v]:
         q.append((v,c+1))
         visited[v] = True

if answerFound:
   print(count)
else:
   print("use the stairs")
