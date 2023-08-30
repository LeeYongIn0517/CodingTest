#2309번
import sys
import itertools
input = sys.stdin.readline
listA = []
for _ in range(9):
   listA.append(int(input()))

result = []
comb = itertools.combinations(listA, 7)

for i in comb:
   if sum(i) == 100:
      result = list(i)
      result.sort()
      for j in result:
         print(j)
      break
