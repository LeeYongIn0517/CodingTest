#1717번
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
n,m = map(int, input().split())
arr = [i for i in range(n+1)]
def find(x):
   if arr[x] != x:
      arr[x] = find(arr[x])
   return arr[x]
def union(a,b):
   a = find(a)
   b = find(b)
   if a < b:
      arr[b] = a
   else:
      arr[a] = b

for i in range(m):
   num,a,b = map(int, input().split())
   if num == 0:
      union(a,b)
   else:
      if find(a) == find(b):
         print("YES")
      else:
         print("NO")
