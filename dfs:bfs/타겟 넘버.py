#프로그래머스
def dfs(numbers, target, current_sum, node_index):
  if node_index == len(numbers):
    if current_sum == target:
      return 1
    else:
      return 0
  else:
    return dfs(numbers, target, current_sum + numbers[node_index], node_index + 1) + dfs(numbers, target,current_sum - numbers[node_index], node_index + 1)
def solution(numbers, target):
  answer = 0
  index = 0
  answer = dfs(numbers, target, 0, 0)
  return answer