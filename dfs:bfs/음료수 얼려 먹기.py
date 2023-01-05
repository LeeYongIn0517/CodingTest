n,m = map(int, input().split())
graph=[]
for i in range(n):
  graph.append(list(map(int, input())))


#dfs
def dfs(x,y):
  if x<=-1 or y<= -1 or x>=n or y>=m:
    return False
  if graph[x][y] == 0:
    graph[x][y] = 1
    #상
    dfs(x-1,y)
    #하
    dfs(x+1,y)
    #좌
    dfs(x,y-1)
    #우
    dfs(x,y+1)
    return True
  return False

#모든 노드(위치)에 대해 음료수 채우기
result =0
for i in range(n):
  for j in range(m):
    if dfs(i,j) == True:
      result+=1
print(result)

