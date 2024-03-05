#11054번
n = int(input())
a = list(map(int, input().split()))
result = [1] * n
reverse_result = [1] * n
answer = 0
for i in range(n):
   for j in range(i):
      if a[i] > a[j]:
         result[i] = max(result[i], result[j]+1)


for i in range(n-1,-1,-1):
   for j in range(n-1,i,-1):
      if a[i] > a[j]:
         reverse_result[i] = max(reverse_result[i],reverse_result[j]+1)

for i in range(n):
   answer = max(answer, result[i] + reverse_result[i]-1)
print(answer)