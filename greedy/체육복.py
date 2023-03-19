import heapq


def only_size(m):
  if m >= 0:
    return m
  else:
    return -m


def solution(n, lost, reserve):
  answer = 0
  able_to_rent = []
  still_need = []
  who_get_rent = 0
  # 여벌x + 도난당함 힙큐 초기화
  for i in lost:
    if i not in reserve:
      heapq.heappush(still_need, i)
  answer += n - (len(still_need))
  # 도난 안 당함 + 빌려줄 수 있는 힙큐 초기화
  for i in reserve:
    if i not in lost:
      heapq.heappush(able_to_rent, i)

  # 핵심 논리
  while still_need:
    lost_item = heapq.heappop(still_need)
    rent_item = heapq.heappop(able_to_rent)
    if only_size(rent_item - lost_item) == 1:
      answer += 1
    else:
      heapq.heappush(able_to_rent, rent_item)

  return answer