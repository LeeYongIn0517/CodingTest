space = int(input())
data = input().split()

x,y = 1,1

#L,R,U,D에 따른 이동방향
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

for move in data:
    
    for i in range(len(move_types)):
        #일치하는 move_types 원소의 x, y 좌표값 더하기(임시)
        if move == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            break

    #공간 이탈 시 좌표반영 안 하고 다음 data원소로 이
    if nx < 1 or nx > space or ny < 1 or ny > space:
        continue
    #좌표 이동
    x, y = nx, ny
            
print(x, y)
