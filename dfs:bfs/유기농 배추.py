#1012번
from collections import deque

t = int(input())
dx=[1,-1,0,0]
dy=[0,0,1,-1]

for i in range(t):
   m,n,k = map(int, input().split())
   locate = []
   for j in range(k):
      x,y = map(int, input().split())
      locate.append((x,y))

 

