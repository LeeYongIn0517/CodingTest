#5430번
import sys
from collections import deque
read = sys.stdin.readline
t = int(read())

for i in range(t):
   func = read()
   n = int(read())
   data = read().rstrip()[1:-1].split(",")

   if n == 0:
      data = []

   queue = deque(data)

   error = False
   countR = 0
   isSuccess = True
   for i in func:
      if i == 'R':
         countR += 1
      if i == 'D':
         if len(queue) == 0:
            print('error')
            isSuccess = False
            break
         else:
            if countR % 2 == 0:
               queue.popleft()
            else:
               queue.pop()
   if isSuccess:
      if countR % 2 != 0:
         queue.reverse()
      print("["+",".join(queue)+"]")
