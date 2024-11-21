#2019 카카오 개발자 겨울 인턴십
import re


def solution(s):
   # 빈도수를 저장할 딕셔너리를 초기화한다
   num_count = dict()
   s = s.replace("{", "").replace("}", "").split(",")
   for c in s:
      # 문자열을 정수로 변환합니다.
      c = int(c)

      # 딕셔너리에 숫자가 이미 존재하면 빈도수를 증가시키고,
      # 그렇지 않으면 새로운 키-값 쌍을 추가한다
      if c in num_count:
         num_count[c] += 1
      else:
         num_count[c] = 1
   # 딕셔너리의 키를 빈도수가 높은 순으로 정렬한다.
   result = sorted(num_count, key=lambda x: num_count[x], reverse=True)

   return result