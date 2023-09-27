#16113번
n = int(input())
a = input()
array = []
garo = int(len(a) / 5)

zero = ['#####','#...#',"#####"]
one = ['#####']
two = ['#.###','#.#.#','###.#']
three = ['#.#.#','#.#.#',"#####"]
four = ['###..','..#..','#####']
five = ['###.#','#.#.#','#.###']
six = ['#####','#.#.#','#.###']
seven = ['#....','#....','#####']
eight = ['#####', '#.#.#', '#####']
nine = ['###.#', '#.#.#', '#####']

numbers = []
answer = ''
prev_i = 0
for i in range(garo,len(a)+1,garo):
   l = list(a[prev_i:i])
   array.append(l)
   prev_i = i

display = zip(*array)
tmp = []
for i,v in enumerate(display):
   t = ''.join(list(v))
   if t == '.....':
      numbers.append(tmp)
      tmp = []
   else:
      tmp.append(t)
numbers.append(tmp)

for i,v in enumerate(numbers):
   if v == zero:
      answer += '0'
   elif v == one:
      answer += '1'
   elif v == two:
      answer += "2"
   elif v == three:
      answer += '3'
   elif v == four:
      answer += "4"
   elif v == five:
      answer += '5'
   elif v == six:
      answer += "6"
   elif v == seven:
      answer += '7'
   elif v == eight:
      answer += "8"
   elif v == nine:
      answer += "9"

print(answer)
