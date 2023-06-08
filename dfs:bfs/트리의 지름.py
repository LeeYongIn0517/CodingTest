import sys
from sys import stdin

input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n = int(stdin.readline())

graph = [[] for _ in range(n+1)]
distance = [-1] * (n+1)
distance[1] = 0

for i in range(n-1):
   a, b, c = map(int, stdin.readline().split())
   graph[a].append((b,c))
   graph[b].append((a,c))
def dfs(x, w):
   for i in graph[x]:
      a, b = i
      if distance[a] == -1:
         distance[a] = b + w
         dfs(a, w+b)

dfs(1,0)


start = distance.index(max(distance))
distance = [-1] * (n+1)
distance[start] = 0
dfs(start, 0)

print(max(distance))
