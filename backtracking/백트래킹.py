#9663번
import sys
n = int(sys.stdin.readline())
board = [0]*15
count = 0
#유망한지 판단하는 함수
def promising(cdx):
   #같은 열이면 안되고, 대각선상에 있어서도 안됨
   for i in range(cdx):
      if (board[cdx] == board[i]) or (abs(cdx - i) == abs(board[cdx] - board[i])):
         return False
   return True

#백트래킹 알고리즘 수행
def backtracking(cdx):
   global count
   #i가 마지막행까지 수행하고 여기까지 오면, 찾기 완료
   if cdx == n:
      count += 1
      return
   for i in range(n):
      #cdx번째 행, i번째 열에 queen을 놓아본다.
      board[cdx] = i
      #cdx의 i번째 자리에 두어도 괜찮으면~
      if(promising(cdx)):
         #그 다음 행에 대해 퀸을 놓기 시작
         backtracking(cdx+1)

backtracking(0)
print(count)