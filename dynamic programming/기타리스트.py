#1495번
import sys
n, s, m = map(int,sys.stdin.readline().split())
v = list(map(int, sys.stdin.readline().split()))
dp = [[0] * (m+1) for _ in range(n+1)]
dp[0][s] = 1

for i in range(n):
   for j in range(m+1):
      if dp[i][j] == 1:
         if j + v[i] <= m:
            dp[i + 1][j + v[i]] = 1
         if j - v[i] >= 0:
            dp[i + 1][j - v[i]] = 1
answer = -1
for i in range(m,-1,-1):
   if dp[n][i] == 1:
      answer = i
      break
print(answer)