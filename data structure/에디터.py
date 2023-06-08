left = list(input())
n = int(input())
right = []
list = []

for i in range(n):
   list.append(input())

for item in list:
   if item[0] == 'P':
      left.append(item[-1])
   elif item == 'L':
      if len(left) > 0:
         word = left.pop()
         right.append(word)
   elif item == 'D':
      if len(right) > 0:
         word = right.pop()
         left.append(word)
   elif item == 'B':
      if len(left) > 0:
         left.pop()

right.reverse()
print("".join(left)+"".join(right))