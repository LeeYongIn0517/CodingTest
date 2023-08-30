#1764번
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nList, mList = [],[]
result = []

for _ in range(n):
   txt = input()
   nList.append(txt[:-1])
nSet = set(nList)

for _ in range(m):
   txt = input()
   mList.append(txt[:-1])
mSet = set(mList)

result =list(nSet&mSet)
result.sort()
print(len(result))
for i in result:
   print(i)