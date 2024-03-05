#11582번
import sys
n = int(input())
data = list(map(int, sys.stdin.readline().split()))
k = int(input())

while True:
    x = k // 2
    l = k // x
    for i in range(1,x+1):
       list= []
       for j in range(1, l+1):
         list.append(data[x*i - j])
       list.sort()
       print(list)