#12851번
import sys
from collections import deque
n,k = map(int, sys.stdin.readline().split())
arr = [-1]*100001
result = 0
def solve(x):
   global result
   q = deque()
   q.append(x)
   arr[x] = 0
   while q:
      x = q.popleft()
      if x == k:
         result += 1
         continue

      for nx in (x*2, x+1, x-1):
         if 0 <= nx < 100001 and (arr[nx] == arr[x]+1 or arr[nx] == -1): #범위에 맞고, 방문한 적이 있거나 이전에 방문한 경우도 포함
            arr[nx] = arr[x]+1
            q.append(nx)

solve(n)
print(arr[k])
print(result)