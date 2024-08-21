#1976번
import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline
n = int(input())
m = int(input())
arr = [i for i in range(n+1)]

def find(x):
   if x != arr[x]:
      arr[x] = find(arr[x])
   return arr[x]

def union(a,b):
   a = find(a)
   b = find(b)

   if a < b:
      arr[b] = a
   else:
      arr[a] = b

def checkPlan():
   for i in range(1, len(plan)):
      if parent != find(plan[i]):
         print("NO")
         return
   print("YES")

for i in range(1,n+1):
   tmp = list(map(int, input().split()))
   for j in range(len(tmp)):
      if tmp[j] == 1:
         union(i, j+1)
plan = list(map(int, input().split()))
parent = 0
parent = find(plan[0])
checkPlan()

