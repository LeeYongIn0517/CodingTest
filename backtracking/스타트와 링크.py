import sys

# sys.setrecursionlimit(10**9)
# input = sys.stdin.readline
# n = int(input())
# board = []
# total_sum = 0
# mini_result = 10**9
# for i in range(n):
#    tmp = list(map(int, input().split()))
#    board.append(tmp)
#    total_sum += sum(tmp)
#
# a_team = []
# b_team = []
# def backtracking(a_depth, a_sum, a_team):
#    global mini_result
#    if len(a_team) == int(n/2):
#       b_sum = 0
#       b_team = []
#       for i in range(1,n+1):
#          if i not in a_team:
#             b_team.append(i)
#          if len(b_team) > 1:
#             for j in b_team:
#                b_sum += board[j - 1][i - 1]
#                b_sum += board[i - 1][j - 1]
#       #팀 점수차이
#       mini_result = min(mini_result, abs(a_sum-b_sum))
#       # print('a_team:{0}'.format(a_team))
#       # print('b_team:{0}'.format(b_team))
#       # print('abs(a_sum-b_sum):{0}'.format(abs(a_sum-b_sum)))
#       # print('mini_result:{0}'.format(mini_result))
#       return
#
#    for i in range(1,n+1):
#       tmp_a_sum = 0
#       if i not in a_team:
#          a_team.append(i)
#
#          if len(a_team) > 1:
#             for j in a_team:
#                tmp_a_sum += board[i-1][j-1]
#                tmp_a_sum += board[j-1][i-1]
#          backtracking(a_depth + 1, a_sum + tmp_a_sum, a_team)
#
#       if len(a_team) > 0:
#          a_team.pop()
#
# backtracking(0, 0, a_team)
# print(mini_result)

#-------------답-------------
import sys
n = int(sys.stdin.readline())
graph = [ list(map(int, sys.stdin.readline().split())) for _ in range(n) ]
visit = [ False for _ in range(n) ]
#최소값을 갱신할 변수 생성
min_value = sys.maxsize

def backTracking(depth, idx):
   global min_value
   if depth == n //2:
      power1, power2 = 0,0
      for i in range(n):
         for j in range(n):
            if visit[i] and visit[j]:
               power1 += graph[i][j]
            elif not visit[i] and not visit[j]:
               power2 += graph[i][j]
      min_value = min(min_value, abs(power1-power2))
      return

   for i in range(idx, n):
      if not visit[i]:
         visit[i] = True
         backTracking(depth+1, i+1)
         visit[i] = False

backTracking(0,0)
print(min_value)