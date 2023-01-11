s = input()
other_count = 0
tmp = s[0]
result = 0
for i in range(len(s)):
  #바뀔 때 체크해주면 됨
  if tmp != s[i]:
    other_count += 1
  tmp = s[i]
#달라지는 부분이 짝수개 일때
if other_count % 2 == 0:
  result = other_count/2
#달라지는 부분이 홀수개 일때
else:
  result = (other_count + 1)/2
print(int(result))