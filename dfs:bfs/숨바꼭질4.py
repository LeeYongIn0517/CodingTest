#13913번
import sys
from collections import deque
n,k = map(int, sys.stdin.readline().split())
MAX = 100001
arr = [-1]*MAX
visited = [-1]*MAX #방문여부 확인 + 인덱스 방문 전 어디인덱스에서 왔는지 주소확인
path = []
def solve(x):
   q = deque()
   q.append(x)
   arr[x] = 0
   visited[x] = x
   while q:
      x = q.popleft()
      if x == k:
         idx = x
         while idx != n:
            path.append(idx)
            idx = visited[idx]
         path.append(n) #첫 시작점까지 넣기
         print(arr[x])
         break

      for nx in (x*2, x+1, x-1):
         if 0 <= nx < MAX and (arr[nx] == arr[x]+1 or arr[nx] == -1): #범위에 맞고, 방문한 적이 있거나 이전에 방문한 경우도 포함
            arr[nx] = arr[x]+1
            visited[nx] = x
            q.append(nx)

solve(n)
print(*path[::-1]) #뒤에서부터 출력5 17
