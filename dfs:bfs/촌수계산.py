from collections import deque
#2644번
n = int(input())
start, end = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
q = deque()
answer = 0
for _ in range(m):
   x,y = map(int, input().split())
   graph[x].append(y)
   graph[y].append(x)

def dfs(count, nodeIdx):
   q.append((count, nodeIdx))
   visited[nodeIdx] = True

   while q:
      count, nodeIdx = q.popleft()
      if nodeIdx == end:
         return count
      nodeList = graph[nodeIdx]
      for i, v in enumerate(nodeList):
         if not visited[v]:
            q.append((count + 1, v))
            visited[v] = True

   return -1

print(dfs(0,start))