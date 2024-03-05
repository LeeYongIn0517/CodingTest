#14002번

n = int(input())
a = list(map(int, input().split()))
result = []
LIS = [a[0]]

def findIdx(item):
   start,end = 0,len(LIS)

   while start < end:
      mid = (start + end) // 2
      if LIS[mid] == item:
         return mid
      elif LIS[mid] < item:
         start = mid+1
      else:
         end = mid-1

   return start

for idx,item in enumerate(a):
   if LIS[-1] < item:
      LIS.append(item)
      result.append(LIS)
   elif LIS[-1] > item:



print(len(LIS))
print(*LIS)