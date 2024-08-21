#2606번
import sys

def find_parent(parents, x):
    if parents[x] != x:
        parents[x] = find_parent(parents, parents[x])
    return parents[x]

def union_parent(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

# 컴퓨터의 수
n = int(sys.stdin.readline())

# 부모 테이블 초기화
parents = [0] * (n + 1)
for i in range(1, n + 1):
    parents[i] = i

# 연결된 컴퓨터 쌍의 수
c = int(sys.stdin.readline())

# 입력값을 받고 부모 합치기 연산 수행
for _ in range(c):
    a, b = map(int, sys.stdin.readline().strip().split())
    union_parent(parents, a, b)

# 부모 테이블이 업데이트되지 않은 경우를 위해 각각의 노드에 대해 부모 찾기 연산 수행
for i in range(1, n + 1):
    find_parent(parents, i)

# 1번 컴퓨터와 부모가 같은 컴퓨터의 개수 세기
print(parents.count(parents[1]) - 1)