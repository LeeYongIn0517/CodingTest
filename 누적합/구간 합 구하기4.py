#11659번
n,m = map(int, input().split())
arr = list(map(int, input().split()))
terms = [list(map(int, input().split())) for _ in range(m)]

for i in range(1, len(arr)):
   arr[i] = arr[i-1] + arr[i]

for item in terms:
   s,e = item[0]-1, item[1]-1
   if(s-1) >= 0:
      print(arr[e] - arr[s-1])
   else:
      print(arr[e])