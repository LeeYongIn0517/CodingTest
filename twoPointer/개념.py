n = 5 # 데이터의 개수 N
m = 5 # 찾고자하는 부분합 M

count = 0
interval_sum = 0
end = 0
data = [1,2,3,2,5]

# start를 차례대로 증가시키며 반복
for start in range(n):
   while interval_sum < m and end < n:
      #end만큼 이동시키기
      interval_sum += data[end]
      end += 1
   #부분합이 m일 때 카운트 증가
   if interval_sum == m:
      count += 1
   interval_sum -= data[start]

print(count)