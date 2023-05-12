#2579번
import sys
n = int(sys.stdin.readline())
list = [int(sys.stdin.readline())  for _ in range(n)]
dp = [0] * n

if n <= 2:
      print(sum(list))
else:
      dp[0] = list[0]
      dp[1] = list[0] + list[1]
      for i in range(2,n):
            dp[i] = max(dp[i-2]+list[i], dp[i-3]+list[i-1]+list[i])
      print(dp[n-1])