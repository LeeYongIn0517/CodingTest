#1700번
n, k = map(int, input().split())
if n >= k:
   print(0)
   exit()

elec_list = list(map(int,input().split()))
plug = set()
cnt = 0

def find_latest(idx):
   result = 0
   max_idx = -1 #가장 나중에 쓰이는 플러그의 인덱스 값 => 최후값 이라 하자
   for num in plug: #콘센트 순차탐색
      try:
         num_idx = elec_list[idx:].index(num) #현재 꽂아야하는 플러그 이후의 원소들 중에서 플러그와 일치하는 num_idx를 선정한다
      except:
         num_idx = k
      if max_idx < num_idx: #최후 값 갱ㅇ신
         result, max_idx = num, num_idx

   return result

for idx, num in enumerate(elec_list):
   plug.add(num) #플러그에 꽂는다
   if len(plug) > n: #한 개를 뽑아야 하면
      cnt += 1 #뽑는 횟수 증가
      latest_used = find_latest(idx) #나중에 쓰여야하는 것을 뽑는다
      plug.discard(latest_used) #그걸 버린다

print(cnt)