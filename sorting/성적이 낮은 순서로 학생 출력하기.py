n = int(input())
data =[]
for i in range(n):
  input_data = input().split()
  data.append((input_data[0], int(input_data[1])))

#키(key)를 이용하여, 점수를 기준으로 정렬
data = sorted(data, key=lambda student: student[1])

#정렬이 수행된 결과를 출력
for student in data:
  print(student[0], end=' ')
