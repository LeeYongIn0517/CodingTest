#11055번
import copy

n = int(input())
arr = list(map(int, input().split()))
result = copy.deepcopy(arr)

for i in range(n):
   for j in range(i):
      if arr[i] > arr[j]:
         result[i] = max(result[j]+arr[i], result[i])

print(max(result))