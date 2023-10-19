#15651번
n,m = map(int,input().split())
l = [i+1 for i in range(n)]
answer = []
arr = []
def backtracking(depth,numbers):
   tmp = [tv for ti,tv in enumerate(numbers)]
   if depth == m:
      answer.append(tmp)
      return

   for li,lv in enumerate(l):
      tmp.append(lv)
      backtracking(depth+1, tmp)
      tmp.pop()

backtracking(0,arr)

for idx,items in enumerate(answer):
   for _,item in enumerate(items):
      print(item, end=' ')
   print()