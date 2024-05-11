import sys

input = sys.stdin.readline
n = int(input())
l = []
for _ in range(n):
   t = list(map(int,input().split()))
   l.append((t[0],t[1]))
l.sort(key = lambda x: (x[1], x[0]))

count = 1
check = l[0][1]
for i in range(1,n):
   s,e = l[i][0], l[i][1]
   if(s >= check):
      count += 1
      check = e

print(count)