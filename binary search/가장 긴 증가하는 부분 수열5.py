#14003번







n = int(input())
A = list(map(int, input().split()))

LIS = [A[0]]
LIS_TOTAL = []
result = []
def findPlace(e):
   start = 0
   end = len(LIS) - 1

   while start <= end:
      mid = (start + end) // 2

      if LIS[mid] == e:
         return mid
      elif LIS[mid] < e:
         start = mid + 1
      else:
         end = mid - 1

   return start

for item in A:
   if LIS[-1] < item:
      LIS.append(item)
      LIS_TOTAL.append( (item,len(LIS)-1) )
   else:
      idx = findPlace(item) # bisect_left(LIS, item)도 가능함.
      LIS[idx] = item
      LIS_TOTAL.append( (item,idx) )

value,order = LIS_TOTAL[-1]
for i in range(len(LIS_TOTAL)-1,-1,-1):
   v,o = LIS_TOTAL[i]
   if(o == order):
      result.append(v)
      order -= 1

print(len(result))
print(*result[::-1])

