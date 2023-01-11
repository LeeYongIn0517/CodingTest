n = int(input())
array = [0] * 1000001
#가게에 있는 전체 부품 번호를 입력받아서 기록
for i in input().split():
  array[int(i)] = 1

m = int(input())
request = list(map(int, input().split()))

for i in request:
  if array[i] == 1:
    print("yes", end=' ')
  else:
    print("no", end=' ')