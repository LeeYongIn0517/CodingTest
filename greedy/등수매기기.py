#백준2012번
import sys
n = int(sys.stdin.readline())
ranking = [i for i in range(1, n+1)]
result = 0
list = [int(sys.stdin.readline()) for x in range(n)]

list.sort()
for i in range(n):
  result += abs(list[i] - ranking[i])

print(result)