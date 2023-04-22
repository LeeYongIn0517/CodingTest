#백준 2293번
import sys
n, k = map(int, sys.stdin.readline().split())
list = [int(input()) for _ in range(n)]
dp = [0]*(k+1)

dp[0] = 1
for j in list:
  for i in range(1,k+1):
    if i-j >= 0:
      dp[i] += dp[i-j]

print(dp[k])