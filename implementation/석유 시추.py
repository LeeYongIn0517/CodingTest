from collections import deque

def solution(land):
    answer = 0
    m = len(land)
    n = len(land[0])
    d = [[0,1], [0,-1], [1,0], [-1,0]]
    visited = [[0]*n for _ in range(m)]
    dic = {}
    amount = 0
    _id = 0
    for i in range(m):
        for j in range(n):
            q = deque()
            if visited[i][j] == 0 and land[i][j] == 1:
                _id += 1
                amount += 1
                q.append((i,j))
                visited[i][j] = 1
                land[i][j] = (_id,_id)
                while q:
                    y,x = q.pop()
                    for k in range(4):
                        ny,nx = d[k][0]+y,d[k][1]+x
                        if 0<=ny<m and 0<=nx<n and visited[ny][nx] == 0 and land[ny][nx] == 1:
                            q.append((ny,nx))
                            amount += 1
                            visited[ny][nx] = 1
                            land[ny][nx] = (_id,_id)
                dic[_id] = amount
                amount = 0
    answer = 0
    for i in range(n):
        _set = set()
        tmp_answer = 0
        for j in range(m):
            if land[j][i]!=0 and land[j][i]!=1:
                _id,_id = land[j][i]
                _set.add(_id)
        for _key in _set:
            tmp_answer += dic[_key]
        answer = max(answer, tmp_answer)
    return answer