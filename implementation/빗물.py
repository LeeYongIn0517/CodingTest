#14719번
import sys
h, w = map(int, sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().split()))
block = [[0 for _ in range(w)] for _ in range(h)]

for i in range(len(data)):
   for j in range(h-data[i], h):
      block[j][i] = 1
#상하좌우
x = [0,0,-1,1]
y = [-1,1,0,0]
result = 0
for j in range(h):
   cnt=0
   cntDoing=False
   for i in range(w):
      if block[j][i] == 1:
         #벽이 처음 나온 경우
         if not cntDoing: cntDoing = True
         #빈칸을 세다가 벽이 나온 경우
         elif cntDoing == True and cnt!=0:
            result += cnt
            cnt = 0 #초기화
      if block[j][i] == 0:
         #빈칸을 세야하는 경우
         if cntDoing: cnt += 1

print(result)