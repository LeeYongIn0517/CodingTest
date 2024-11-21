#2021 카카오 블라인드
from collections import Counter
from itertools import combinations
def solution(orders, course):
   answer = []

   for c in course:
      # 각 주문에 대해 조합 생성 후 모두 합침
      all_combinations = []
      for order in orders:
         all_combinations += combinations(sorted(order), c)

      # 가장 많이 선택된 조합을 필터링
      most_common_combinations = Counter(all_combinations).most_common()
      max_count = most_common_combinations[0][1] if most_common_combinations else 0

      # 최소 2번 이상 주문된 조합만 결과에 추가
      for combination, count in most_common_combinations:
         if count >= 2 and count == max_count:
            answer.append("".join(combination))

   return sorted(answer)