#10986번
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))
sum = 0
numRemainder = [0] * M

for i in range(N):
   sum += num[i]
   numRemainder[sum % M] += 1 #누적합 값의 나머지를 구하고 그 나머지를 빈도수를 카운트

result = numRemainder[0]
for i in numRemainder: #나머지가 없는 것의 빈도수만큼 반복
   result += i * (i - 1) // 2 #조합 이용해서 카운트

print(result)