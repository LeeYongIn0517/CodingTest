#2606번
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
q = []
count = 0
for _ in range(m):
   v1, v2 = map(int,input().split())
   graph[v1].append(v2)
   graph[v2].append(v1)

q.append(1)
visited[1] = True
while q:
   idx = q.pop()
   l = graph[idx]
   for i,x in enumerate(l):
      if not visited[x]:
         q.append(x)
         count += 1
         visited[x] = True
print(count)