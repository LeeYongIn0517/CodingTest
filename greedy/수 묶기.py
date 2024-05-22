#1744번
import sys

input = sys.stdin.readline
n = int(input())
parr = []
marr = []
res = 0
for i in range(n):
    a = int(input())
    if a == 1: #1일 경우 바로 더해줌
        res += 1
    elif a > 0:
        parr.append(a)
    else: #0또는 음수인 경우
        marr.append(a)
parr.sort() #오름차순
marr.sort(reverse=True) #내림차순
while len(parr) != 0:
    if len(parr) == 1:#양수가 하나밖에 없는 경우니까
        res += parr.pop()
    else:
        res += parr.pop() * parr.pop() #큰 양수끼리 곱해줌
while len(marr) != 0:
    if len(marr) == 1:
        res += marr.pop()
    else:
        res += marr.pop() * marr.pop()
print(res)