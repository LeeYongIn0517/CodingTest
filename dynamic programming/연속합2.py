#13398번
n = int(input())
arr = list(map(int, input().split()))
#dp[0]은 이전 문제와 동일한 점화식, 원소 하나를 제거한 dp[1]은 새로운 점화식
dp = [[0] * n for _ in range(2)] #dp[1][0] = 0
dp[0][0] = arr[0]
answer = arr[0]
for i in range(1,n):
    dp[0][i] = max(dp[0][i-1]+arr[i],arr[i])
    dp[1][i] = max(dp[1][i-1]+arr[i], dp[0][i-1])
    answer = max(answer, dp[0][i], dp[1][i])
print(answer)