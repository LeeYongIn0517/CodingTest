#백준 1715번
import heapq
from collections import deque
n = int(input())
list=[]

for _ in range(n):
  heapq.heappush(list,int(input()))

result = 0
while len(list) > 1:
  a = heapq.heappop(list)
  b = heapq.heappop(list)
  last_sum = a + b
  result += last_sum
  heapq.heappush(list, last_sum)
print(result)