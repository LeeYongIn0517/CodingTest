#2021 카카오 블라인드
from itertools import combinations
from bisect import bisect_left


def solution(info, query):
   answer = []
   dictionary = {}  # {조건:[점수]}
   for i in info:
      i = i.split(' ')
      for j in range(5):
         combi = list(combinations(i[:4], j))
         for com in combi:
            str_value = " ".join(list(com))
            if str_value in dictionary:
               dictionary[str_value].append(int(i[4]))
            else:
               dictionary[str_value] = [int(i[4])]

   # 이진탐색을 위해 미리 딕셔너리의 value값들 정렬
   for key in dictionary:
      dictionary[key].sort()

   answer = []
   for q in query:
      q = q.split(" and ")
      value = q[3].split(' ')  # '음식 점수' 나누기
      q[3] = value[0]

      str_value = []  # 딕셔너리 키 완성하기
      for i in q:
         if i != '-':
            str_value.append(i)
      str_value = " ".join(str_value)

      if str_value in dictionary:
         result = dictionary[str_value]
         answer.append(len(result) - bisect_left(result, int(value[1])))  # 점수를 기준으로 이진탐색해서 인원계산
      else:
         answer.append(0)

   return answer