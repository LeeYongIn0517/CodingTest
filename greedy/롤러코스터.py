#2873번
import sys
input = sys.stdin.readline
r,c = map(int, input().rstrip().split())
arr = [ list(map(int, input().rstrip().split())) for _ in range(c)]

if r == 2 and c == 2:
   if arr[1][0] > arr[0][1]:
      print("DR")
   else:
      print("RD")

answer = ""
t = 0
if c % 2 == 0:
   t = c-2
else:
   t = c-1
for i in range(c-1):
   if i % 2 == 0:
      answer += "R"*(r-1)
   else:
      answer += "L"*(r-1)
   if i != c-1:
      answer += "D"

if r == 2:
   for token in answer:
      if token == "L":
         print("U")
      elif token == "U":
         print("L")
      elif token == "R":
         print("D")
      elif token == "D":
         print("R")
else:
   print(answer)