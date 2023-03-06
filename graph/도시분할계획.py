def find_parent(parent, x):
  if (parent[x] != x):
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)

  if b > a:
    parent[b] = a
  else:
    parent[a] = b

#입력받기
n, m = map(int, input().split())
#필요한 배열 및 결과값 초기화
edges = []
result = 0
parent = [0] * (n+1)
#a부터 b까지의 거리비용 cost
for _ in range(m):
  a, b, cost = map(int, input().split())
  edges.append((cost, a, b))

#간선을 비용순으로 정렬
edges.sort()
last = 0 #최소 신장 트리에 포함되는 간선 중에서 가장 비용이 큰 간선

for i in range(n):
  parent[i] = i

for edge in edges:
  cost, a, b = edge
  #사이클이 발생하지 않는 경우에만 집합에 포함
  if(find_parent(parent, a) != find_parent(parent, b)):
    union_parent(parent, a, b)
    result += cost
    last = cost

#답 출력
print(result - last)