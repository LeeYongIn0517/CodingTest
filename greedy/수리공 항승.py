#1449번
import sys
n, l = map(int, input().split())
list = list(map(int, sys.stdin.readline().split()))
list.sort()
location = 0
tape_end = list[0] + l - 1
count = 1
for target in list:
  location = target
  if location <= tape_end:
    continue
  elif location > tape_end:
    count += 1
    tape_end = location + l - 1
print(count)