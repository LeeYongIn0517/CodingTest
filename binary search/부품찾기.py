n = int(input())
array = list(map(int, input().split()))
array.sort()
m = int(input())
request = list(map(int, input().split()))

def binary_search(array, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2
  #찾은 경우 중간점 인덱스 반환
  if array[mid] == target:
    return True
  #중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
  elif array[mid] > target:
    return binary_search(array, target, start, mid-1)
  #반대의 경우 오른쪽 확인
  else:
    return binary_search(array, target, mid+1, end)

result = None
for i in request:
  result = binary_search(array, i,0,n-1)
  if result == True: print("yes", end=' ')
  else: print("no", end= ' ')
