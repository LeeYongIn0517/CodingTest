#13701번

arr = [(1<<5) * (2**20)]
n,idx,shift = 0,0,0
l = list(map(int, input().split()))

for i in l:
   idx = i / 32
   shift = i % 32

   if int(arr[idx]) & (1<<shift):
      continue

   print(i)
   arr[idx] += (1 << shift)