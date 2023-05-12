#10816번
import sys
#---------------이진탐색 모듈 bisect 이용하기---------------
# from bisect import bisect_left, bisect_right
# n = int(sys.stdin.readline())
# data = list(map(int, sys.stdin.readline().split()))
# m = int(sys.stdin.readline())
# m_list = list(map(int, sys.stdin.readline().split()))
# data.sort()
#
# def count_by_range(left_value, right_value):
#    right_index = bisect_right(data, right_value) #list에서 value가 들어갈 가장 오른쪽 인덱스 반환
#    left_index = bisect_left(data, left_value) #list에서 value가 들어갈 가장 왼쪽 인덱스 반환
#    return right_index - left_index
#
# for i in m_list:
#    print(count_by_range(i,i), end=" ")

#---------------리스트의 원소가 몇번 나왔는지 세는 Counter 모듈 이용하기---------------
# from collections import Counter
# n = int(sys.stdin.readline())
# data = list(map(int, sys.stdin.readline().split()))
# m = int(sys.stdin.readline())
# m_list = list(map(int, sys.stdin.readline().split()))
#
# #리스트의 원소가 몇 번 등장했는지 세어 딕셔네리 형태로 반환함.
# count = Counter(data)
# print(count)
# for i in range(len(m_list)):
#    if m_list[i] in count:
#       print(count[m_list[i]], end=' ')
#    else:
#       print(0, end=' ')

#---------------직접 해쉬맵을 만들어 구현하기(파이썬에선 해쉬맵이 딕셔너리)---------------
n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

hash = {}

for i in data:
   if i in hash:
      hash[i] += 1
   else:
      hash[i] = 1

for i in range(len(m_list)):
   if m_list[i] in hash:
      print(hash[m_list[i]], end=' ')
   else:
      print(0, end=' ')