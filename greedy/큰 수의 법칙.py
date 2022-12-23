N,M,K = map(int,input().split( ))
data = list(map(int,input().split( )))

answer = 0
first_count = 0
second_count = 0

data.sort()
first = data[N-1]
second = data[N-2]

first_count = (M /(K+1)) * K #큰 수가 더해지는 횟수
second_count = M - first_count #작은 수가 더해지는 횟

answer += first_count * first
answer += second_count * second
print(answer)
