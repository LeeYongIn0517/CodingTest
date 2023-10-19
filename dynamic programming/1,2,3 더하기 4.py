#15989번
import sys
n = int(input())
l = [int(sys.stdin.readline()) for _ in range(n)]
dp = [1 for _ in range(max(l)+1)]
for i in range(2,len(dp)):
   dp[i] += dp[i-2]

for i in range(3,len(dp)):
   dp[i] += dp[i-3]

for k in l:
   print(dp[k])