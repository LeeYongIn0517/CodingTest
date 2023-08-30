#1182번
import sys
from itertools import combinations
sys.setrecursionlimit(10**9)
#-----조합을 활용한 풀이(단순), 브루트포스-----#
# n, s = map(int, sys.stdin.readline().split())
# list = list(map(int, sys.stdin.readline().split()))
# count = 0
# for i in range(1, n+1):
#    comb = combinations(list, i)
#
#    for x in comb:
#       if sum(x) == s:
#          count += 1
# print(count)
#-----재귀함수와 백트래킹을 활용한 풀이------#
n, s = map(int, sys.stdin.readline().split())
list = list(map(int, sys.stdin.readline().split()))
cnt = 0
def subset_sum(idx, sub_sum):
   global cnt

   if idx >= n:
      return

   sub_sum += list[idx]
   if sub_sum == s:
      cnt += 1

   #현재 list[idx]를 선택한 경우의 가지
   subset_sum(idx+1, sub_sum)
   #현재 list[idx]를 선택하지 않은 경우의 가지
   subset_sum(idx+1, sub_sum - list[idx])

subset_sum(0,0)
print(cnt)