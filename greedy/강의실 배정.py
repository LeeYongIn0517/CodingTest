#11000번
import heapq
import sys

input = sys.stdin.readline
N = int(input())
time = []

for _ in range(N):
   time.append(list(map(int, input().split(' '))))
time.sort(key = lambda x: (x[0], x[1]))

heap = [time[0][1]] #첫번째 원소의 끝나는 시간
for i in range(1,N):
   if heap[0] <= time[i][0]: #시간 비교, 강의실 힙타겟의 끝나느 시간이 시간표비교 타켓의 시작시간보다 같거나 작거나 같으면 꺼낸다.왜꺼내지?
      heapq.heappop(heap) #
   heapq.heappush(heap, time[i][1]) #끝나는 시간을 넣어줌

print(len(heap))



