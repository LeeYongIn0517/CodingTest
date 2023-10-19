#11058번
n = int(input())
dp = [0 for _ in range(101)]
dp[1],dp[2],dp[3],dp[4],dp[5],dp[6] = 1,2,3,4,5,6

for j in range(7,n+1):
   dp[j] = max(dp[j-3]*2,dp[j-4]*3, dp[j-5]*4)

print(dp[n])
