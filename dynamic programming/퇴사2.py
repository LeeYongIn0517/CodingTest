import sys
n = int(input())
t,p,m = [0 for _ in range(n+1)],[0 for _ in range(n+1)],[0 for _ in range(n+1)]

for i in range(1,n+1):
   t[i], p[i] = map(int, sys.stdin.readline().split())

for i in range(1,n+1):
   m[i] = max(m[i], m[i-1])
   fin_date = i + t[i] - 1
   if fin_date <= n:
      m[fin_date] = max(m[fin_date], m[i-1]+p[i])

print(max(m))