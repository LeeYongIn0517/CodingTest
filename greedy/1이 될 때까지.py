n, k = map(int, input().split())
count = 0

while True:
    # N % K == 0이 될 때까지 1씩 빼는 걸 수식
    target = (n // k) * k
    count += (n - target)
    n = target
    # 더 이상 못 나누므로 루프 탈출
    if n < k: break
    # K로 나누기
    n //= k
    count += 1
# 마지막으로 남은 숫자 더하기(마지막 한번은 제외. N이 1이 되는게 목적이므로)
count += (n-1)
print(count)
