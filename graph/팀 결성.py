def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)

  if a < b:
    parent[b] = a
  else:
    parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n+1)
answer = []

for i in range(n+1):
  parent[i] = i

for _ in range(m):
  work, a, b = map(int, input().split())
  if work == 0:
    union(parent, a, b)
  elif work == 1:
    if find_parent(parent,a) == find_parent(parent, b):
     answer.append("YES")
    else:
      answer.append("NO")

for i in answer:
  print(i)