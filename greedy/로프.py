#2217번
import sys
input = sys.stdin.readline
n = int(input())
ropes = [ int(input()) for _ in range(n) ]
ropes.sort()

answer = 0
for i in range(n):
   total_w = ropes[i]*(n-i)
   answer = max(answer, total_w)
print(answer)