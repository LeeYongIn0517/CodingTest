#백준 1138번
import sys
n = int(sys.stdin.readline())
result = [0] * n
data = list(map(int,sys.stdin.readline().split()))

for i in range(0,n):
  cnt = 0
  for j in range(n):
    if cnt == data[i] and result[j] == 0:
      result[j] = i+1
      break
    elif result[j] == 0:
      cnt += 1

for i in result:
  print(i, end=" ")