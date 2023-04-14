#백준 2141번

n = int(input())
list = []
total_population = 0
count = 0

for _ in range(n):
  x, a = map(int, input().split())
  list.append([x,a])
  total_population += a

list.sort(key=lambda x:x[0])
for i in range(n):
  count += list[i][1]
  if count >= total_population / 2:
    print(list[i][0])
    break