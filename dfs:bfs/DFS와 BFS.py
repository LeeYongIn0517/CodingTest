#백준 1260번
from collections import deque

n, m, start = map(int,input().split())
#-----------dfs알고리즘--------------
visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]
dfs_result=[]

for i in range(m):
  v1, v2 = map(int, input().split())
  graph[v1].append(v2)
  graph[v2].append(v1)
  graph[v1].sort()
  graph[v2].sort()
def dfs(i):
  visited[i] = True
  dfs_result.append(i)
  for node in graph[i]:
    if visited[node] == False:
      dfs(node)
#-----------bfs알고리즘--------------
visited2 = [False] * (n + 1)
q = deque()
bfs_result=[]

q.append(start)
while q:
  v = q.popleft()
  visited2[v] = True
  bfs_result.append(v)
  for node in graph[v]:
    if visited2[node] == False:
      visited2[node] = True
      q.append(node)

dfs(start)
for i in dfs_result:
  print(i, end=' ')
print()
for i in bfs_result:
  print(i, end=' ')
