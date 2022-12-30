input_data = input()
count = 0
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

for step in steps:
    nx = row + step[1]
    ny = column + step[0]
    if nx >= 1 and ny >= 1 and nx <= 8 and ny <= 8: count += 1
print(count)
