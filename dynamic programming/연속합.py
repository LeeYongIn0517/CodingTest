#1912번
n = int(input())
arr = list(map(int, input().split()))
d=[0 for _ in range(n)]
d[0] = arr[0]
#점화식
for i in range(1,n):
    d[i] = max(arr[i],arr[i]+d[i-1])

print(max(d))