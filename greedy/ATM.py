#11399번
import sys
input = sys.stdin.readline
n = int(input())
l = list(map(int, input().split()))
l.sort()

for i in range(1,n):
   l[i] += l[i-1]
print(sum(l))