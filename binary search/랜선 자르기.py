#1654번
import sys
k, n = map(int, sys.stdin.readline().split())
lan = [int(input()) for _ in range(k)]
start, end = 1, max(lan)


while start <= end:
   mid = (start + end) // 2
   num = 0 #랜선 개수

   for i in lan:
      num += i // mid
   if num >= n:
      start = mid + 1
   else:
      end = mid - 1
print(end)