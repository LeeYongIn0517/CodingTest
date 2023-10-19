#12026번
import sys
n = int(sys.stdin.readline())
l = list(sys.stdin.readline().rstrip())
INF = 1e9
dp = [INF for _ in range(n)]
dp[0] = 0

def getPrev(x):
   if x == 'O':
      return 'B'
   elif x == 'J':
      return 'O'
   elif x == 'B':
      return  'J'

for i in range(1,n):
   prev = getPrev(l[i])
   for j in range(i):
      k = j-i
      if l[j] == prev:
         dp[i] = min(dp[i], dp[j] + k*k)

if dp[-1] == INF:
   print(-1)
else:
   print(dp[-1])