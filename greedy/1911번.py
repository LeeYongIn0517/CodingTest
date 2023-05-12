import sys

n, l = map(int, sys.stdin.readline().split())
list = []
for i in range(n):
   start, end = map(int, sys.stdin.readline().split())
   list.append([start, end])

panel_end = list[0][0] + l
count = 0
for i in range(len(list)):
   target_start = list[i][0]
   target_end = list[i][1]

   if panel_end < target_end:
      panel_end = target_start + l
      count += 1

   while panel_end < target_end:
      panel_end += l
      count += 1

print(count)