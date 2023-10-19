#1759번
l,c = map(int,input().split())
alphabets = list(map(str,input().split()))
alphabets.sort()
moeum = ['a','e','i','o','u']
tmp = []
visited = [False for _ in range(c)]
def backtracking(depth, isMoeumExist, prevIdx, jaeumCnt):
   if depth == l and isMoeumExist and jaeumCnt >= 2:
      print(''.join(tmp))
      return
   previousIdx = prevIdx
   for i,v in enumerate(alphabets):
      if previousIdx < i and not visited[i]:
         tmp.append(v)
         visited[i] = True
         if v in moeum:
            backtracking(depth + 1, True, i, jaeumCnt)
         else:
            backtracking(depth + 1, isMoeumExist, i, jaeumCnt + 1)
         visited[i] = False
         tmp.pop()

backtracking(0, False, -1, 0)