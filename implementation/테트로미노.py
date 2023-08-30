import sys

input = sys.stdin.readline
n, m = map(int, input().split())
array = []
check_array = [0*len(m) for _ in range(n)]
tetro = [ [(0,0),(0,1),(0,1),(0,1)],
        [(0,0),(1,0),(1,0),(1,0)],
        [(),(),(),()],
        [] ]
#상하좌우
x = [0,0,-1,1]
y = [-1,1,0,0]
for i in range(n):
   array.append(list(map(int, input().split())))