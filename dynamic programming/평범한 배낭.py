#12865번
import sys
n, k = map(int, sys.stdin.readline().split())
thing = [[0,0]]
d = [[0] * (k+1) for _ in range(n+1)] #평행우주의 느낌으로 이해하자

for i in range(n):
   thing.append(list(map(int, input().split())))

#물건을 차려대로 집어넣을 지 말지 생각하는 것.
for i in range(1,n+1):
   for j in range(1, k+1):
      w = thing[i][0]
      v = thing[i][1]

      if j < w:
         d[i][j] = d[i-1][j] #이번 가방은 넣지 않는 거로
      else:
         d[i][j] = max(d[i-1][j], d[i-1][j-w]+v)

print(d[n][k])