#백준 11053번
import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
result = [1] * n


for i in range(len(a)):
  for j in range(i):
    if a[i] > a[j]:
      result[i] = max(result[i], result[j]+1)

print(max(result))