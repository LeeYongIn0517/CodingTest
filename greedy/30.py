#106109번
import sys
input = sys.stdin.readline
n = [0,0,0,0,0,0,0,0,0,0,0]
check = 0
for digit in input().rstrip():
   digit = int(digit)
   check += digit
   n[digit] += 1

result = ""
if check % 3 == 0 and n[0] > 0:
   for i in range(len(n)):
      for j in range(n[i]):
         result = str(i) + result
   print(result)
else:
   print(-1)