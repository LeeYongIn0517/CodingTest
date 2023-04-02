#이것이 코딩테스트다
n, m = map(int, input().split())
data = list(map(int, input().split()))
metadata = [0] * 11
count = 0

for item in data:
  metadata[item] += 1

for i in range(1,m):
  n -= metadata[i]
  count += metadata[i] * n

print(count)