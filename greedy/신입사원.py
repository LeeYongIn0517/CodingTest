#1946번
import sys
import heapq

input = sys.stdin.readline
t = int(input())
for _ in range(t):
   n = int(input())
   h = []
   count = 1
   for _ in range(n):
      ele = list(map(int,input().rstrip().split()))
      h.append(ele)
   h.sort(key = lambda x : (x[0], x[1]))
   heapq.heapify(h)

   standard = heapq.heappop(h)
   while h:
      target = heapq.heappop(h)
      if standard[1] > target[1]:
         count += 1
         standard = target
   print(count)