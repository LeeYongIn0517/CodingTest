#프로그래머스 문제, 오류 고쳐서 통과하기!
from collections import deque
def solution(maps):
  answer = 0
  q = deque()
  q.append((0, 0))
  visited = [[False for j in range(len(maps[0]))] for i in range(len(maps))]
  count = 0
  n = len(maps)
  m = len(maps[0])

  def dfs(maps):
    # 상하좌우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    cx, cy = q.popleft()

    for i in range(4):
      nx = cx + dx[i]
      ny = cy + dy[i]

      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        print('좌표초과:{0},{1}'.format(nx, ny))
        continue
      if visited[nx][ny] == True or maps[nx][ny] == 0:
        print('갈수없는곳:{0},{1}'.format(nx, ny))
        continue
      if (nx == n - 1 and ny == m - 1):
        count += 1

    q.append((nx, ny))
    visited[nx][ny] = True

  visited[0][0] = True
  while q:
    dfs(maps)

  if (maps[-1][-1] == 1):
    answer = -1
  else:
    answer = maps[-1][-1]

  return answer