#5557번
import sys
n = int(sys.stdin.readline())
l = list(map(int,sys.stdin.readline().split()))
dp = [[0] * 21 for _ in range(n)]
dp[0][l[0]] = 1

for i in range(1,n):
   for j in range(21):
      if dp[i-1][j]:
          if j + l[i] <= 20:
              dp[i][j+l[i]] += dp[i-1][j]
          if j - l[i] >= 0:
              dp[i][j-l[i]] += dp[i-1][j]

print(dp[n-2][l[n-1]])