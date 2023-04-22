#백준 11052번
import sys

d = [0] * 10000
n = int(input())
p_list = list(map(int,sys.stdin.readline().split()))

for i in range(n):
  d[i+1] = p_list[i]

for i in range(1,n+1):
  for j in range(1,i+1):
    d[i] = max(d[i],d[i-j] + d[j])

print(d[n])