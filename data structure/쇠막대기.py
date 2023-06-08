data = list(input())
answer = 0
stack = []

for i in range(len(data)):
   if data[i] == '(':
      stack.append(data[i])
   else:
      if data[i-1] == '(':
         stack.pop()
         answer += len(stack)
      else:
         answer += 1
         stack.pop()

print(answer)