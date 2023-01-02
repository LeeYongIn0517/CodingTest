n = int(input())
data = list(map(int, input().split()))
##나의 풀이
count =0
nervous_types = [0]* len(data)

for i in data:
    nervous_types[i] += 1
for i in range(1,len(nervous_types)):
    if nervous_types[i] >= i:
        count += nervous_types[i] // i
print('나의 풀이:',count)
##답지 풀이
count2=0
result=0
data.sort()
for i in data:
    count2 += 1
    if count2 >= i:
        result += 1
        count2 = 0
print('답지 풀이:',result)