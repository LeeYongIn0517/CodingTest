#백준 1911번
import sys

n, l = map(int, input().split())
pool = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
pool.sort(key = lambda x:x[0])
plank = pool[0][0]
total_count = 0
for start, end in pool:
  if plank > end:
    continue #이번 웅덩이를 이미 덮어버린 경우->패스
  elif plank < start: #웅덩이 시작 위치까지 널판지가 안 닿음
    plank = start #널판지 위치 갱신
  dist = end - plank #거리 측정
  remainder = 1 #적어도 하나는 필요하다고 가정
  if dist % l == 0: #거리가 딱 l만큼인 경우
    remainder = 0 #밑의 공식 상 0으로 초기화
  count = dist // l + remainder #널판지 몇개 필요한지 계산
  plank += count * l #널판지 끝 위치 갱신
  total_count += count #널판지 개수 갱신
print(total_count)