arr = [3,2,4,4,2,5,2,5,5]
arr.sort()

n = arr[-1]
count = [0] * (n)
final_result = []

for i in arr:
   count[i - 1] += 1

for i in count:
   if i > 1:
      final_result.append(i)

if final_result:
   print(final_result)
else:
   final_result.append(-1)
   print(final_result)
