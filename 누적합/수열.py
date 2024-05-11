#2559번
import sys

n, k = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))
arr2 = []
for j in range(1,len(arr)):
   arr[j] = arr[j] + arr[j-1]

max_num = arr[k-1]
for i in range(k,len(arr)):
   if (i-k) > 0:
      max_num = max(max_num, arr[i] - arr[i - k])

print(max_num)