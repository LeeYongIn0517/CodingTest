#8911번
n = int(input())
l = [input() for _ in range(n)]
#상좌하우 좌로 회전 패턴
direction = [(-1,0),(0,-1),(1,0),(0,1)]
#상,좌,하,우
d = 0
dx = [0,-1,0,1] #total_x
dy = [1,0,-1,0] #total_y
total_x ,total_y = 0,0
answer = []

for i,v in enumerate(l):
   min_x, min_y, max_x, max_y = 0, 0, 0, 0
   x, y, d = 0, 0, 0
   for j,s in enumerate(v):
      if  s == 'F':
         x += dx[d]
         y += dy[d]
      elif s == 'B':
         x -= dx[d]
         y -= dy[d]
      elif s == 'L':
         d = (d+1) % 4
      elif s == 'R':
         d = (d+3) % 4
      min_x = min(min_x, x)
      min_y = min(min_y, y)
      max_x = max(max_x, x)
      max_y = max(max_y, y)

   width = abs(max_x-min_x) * abs(max_y-min_y)
   answer.append(str(width))

print('\n'.join(answer))