#2852번
import sys
n = int(input())
data=[]
for i in range(n):
   team_num, time = sys.stdin.readline().split()
   min = time[0:2]
   sec = time[3:5]
   data.append([team_num,int(min),int(sec)])
data.sort(key=lambda x:x[1])
