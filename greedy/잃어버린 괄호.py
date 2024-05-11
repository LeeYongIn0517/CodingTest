#1541번
import sys, re

input = sys.stdin.readline
q = []
s = input().rstrip().split("-")
for item in s:
   tmp = list(map(int,item.split("+")))
   q.append(sum(tmp))

answer = q[0]
for i in range(1,len(q)):
   answer -= q[i]

print(answer)