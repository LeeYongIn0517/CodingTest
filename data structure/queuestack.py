#백준 24511번 , 시간초과를 해결한 버전인데 이해가... 안간다!
from collections import deque
n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
m = int(input())
C = list(map(int,input().split()))
answer = []

queue = deque([])
for i in range(n):
  if A[i] == 0:
    queue.appendleft(B[i])

for c in C:
    queue.append(c)
    print(queue.popleft(),end = " ")
