#15663번
n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [False] * n
temp = []

def backtracking():
    if len(temp) == m:
        print(*temp)
        return

    remember_me = 0
    for i in range(n):
        if not visited[i] and remember_me != nums[i]:
            visited[i] = True
            temp.append(nums[i])
            remember_me = nums[i]
            backtracking()
            visited[i] = False
            temp.pop()

backtracking()
