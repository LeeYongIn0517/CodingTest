#14888번
import sys
from itertools import permutations
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
#----------- 백트래킹 -----------
n = int(input())
data = list(map(int, input().split()))
operators = list(map(int, input().split()))
maximum = -10**9
minimum = 10**9
def backtracking(depth, result, plus, minus, multi, divide):
   global maximum, minimum
   if depth == n:
      maximum = max(maximum, result)
      minimum = min(minimum, result)

   if plus>0:
      backtracking(depth+1, result + data[depth], plus - 1, minus, multi, divide)
   if minus>0:
      backtracking(depth + 1, result - data[depth], plus, minus - 1, multi, divide)
   if multi>0:
      backtracking(depth + 1, result * data[depth], plus, minus, multi - 1, divide)
   if divide>0:
      backtracking(depth + 1, int(result / data[depth]), plus, minus, multi, divide - 1)

backtracking(1, data[0], operators[0], operators[1], operators[2], operators[3])
print(maximum)
print(minimum)
#----------- 순열로 브루트포스 -----
# n = int(input())
# data = list(map(int, input().split()))
# operators = list(map(int, input().split()))
# oper_type = ['+', '-', '*', '/']
# oper_array = []
# maximum = -10**9
# minimum = 10**9
#
# #oper_array 초기화
# for j in range(len(operators)):
#    for k in range(operators[j]):
#       oper_array.append(oper_type[j])
# def combinating(array):
#    comb_result = permutations(array)
#    global maximum, minimum
#
#    for item in comb_result:
#       result = data[0]
#       for i in range(len(item)):
#          if item[i] == '+':
#             result += data[i+1]
#          elif item[i] == '-':
#             result -= data[i+1]
#          elif item[i] == '*':
#             result *= data[i+1]
#          elif item[i] == '/':
#             result = int(result / data[i+1])
#
#       maximum = max(maximum, result)
#       minimum = min(minimum, result)
#
# combinating(oper_array)
# print(maximum)
# print(minimum)