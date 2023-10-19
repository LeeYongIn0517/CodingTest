# #1890번
import sys
n = int(input())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dx = [0,1] #하,우
dy = [1,0]
dp[0][0] = 1

for i in range(n):
   for j in range(n):
      print('i,j:({0}, {1})'.format(i,j))
      # 현재 탐색하는 좌표가 오른쪽 맨 끝 점이면 반복을 멈춘다.
      if i == n - 1 and j == n - 1:
         print(dp[i][j])
         for item in dp:
            print(item)

      jump = a[i][j]
      for di in range(2):
         ni, nj = i + dy[di]*jump, j + dx[di]*jump
         if ni < n and nj < n:
            dp[ni][nj] += dp[i][j]

print(dp[i][j])
for item in dp:
   print(item)