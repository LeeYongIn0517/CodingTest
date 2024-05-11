#11047번
n, k = map(int,input().split())
ai = [int(input()) for _ in range(n)]

count = 0
money = k
for i in range(len(ai)-1,-1,-1):
   if money >= ai[i]:
      number = money // ai[i]
      money -= number * ai[i]
      count += number
   if money == 0:
      break

print(count)
