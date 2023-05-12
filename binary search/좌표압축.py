#188870번
import copy
import sys
n = int(input())
data = list(map(int,sys.stdin.readline().split()))
sorted_data = copy.deepcopy(data)
sorted_data = list(set(sorted_data)) #중복원소 제거
sorted_data.sort(reverse=False) #[-10, -9, 2, 4, 4]

def binary_search(array, start, end, target):
   while start <= end:
      mid = (start+end) // 2
      if array[mid] == target:
         return mid
      elif array[mid] < target:
         start = mid + 1
      elif array[mid] > target:
         end = mid - 1
   return None

for i in data:
   result = binary_search(sorted_data, 0, len(sorted_data)-1, i)
   print(result, end=" ")