#13335번
import sys

n, w, l = map(int, sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
temp = [0] * w #다리의 칸
cnt = 0

#반복문을 통해 다리의 모든 트럭이 지나갈 때까지 반복
while temp:
   cnt += 1 #카운트
   temp.pop(0) #다리의 칸을 하나씩 줄인다.

   #모든 트럭을 확인
   if arr:
      if sum(temp) + arr[0] > l:
         temp.append(0)
      else:
         temp.append(arr.pop(0))

print(cnt)