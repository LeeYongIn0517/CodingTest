arr = ["INT", "INT", "BOOL", "SHORT", "LONG"]
#arr = ["INT", "SHORT", "FLOAT", "INT", "BOOL"]
#arr = ["FLOAT", "SHORT", "BOOL", "BOOL", "BOOL", "INT"]
#arr = ["BOOL", "LONG", "SHORT", "LONG", "BOOL", "LONG", "BOOL","LONG","SHORT","LONG","LONG"]
new_arr = []
result = []
piece = ""
MAX_BYTE = 8
total_byte = 0

def putMorePadding(curIdx, nextIdx):
   global piece, MAX_BYTE
   paddings = ""
   if new_arr[curIdx] < MAX_BYTE and len(piece) + new_arr[nextIdx] > MAX_BYTE:
      for i in range(MAX_BYTE-len(piece)):
         paddings += "."
   return paddings

def putHashTag(i):
   global piece
   if new_arr[i] == 1:
      return "#"
   elif new_arr[i] == 2:
      return "##"
   elif new_arr[i] == 4:
      return "####"
   elif new_arr[i] == 8:
      return "########"
   elif new_arr[i] == 16:
      return "########,########"

for i in arr:
   if i == "BOOL":
      new_arr.append(1)
      total_byte += 1
   elif i == "SHORT":
      new_arr.append(2)
      total_byte += 2
   elif i == "FLOAT":
      new_arr.append(4)
      total_byte += 4
   elif i == "INT":
      new_arr.append(8)
      total_byte += 8
   elif i == "LONG":
      new_arr.append(16)
      total_byte += 16

if total_byte > 128:
   print("HALT")
else:
   for i in range(len(new_arr)-1):
      piece += putHashTag(i)
      print(piece)
      if new_arr[i] == 1:
         if new_arr[i + 1] == 2:
            piece += "."
         elif new_arr[i + 1] == 4:
            piece += "..."

      piece += putMorePadding(i,i + 1)
      if len(piece) == MAX_BYTE:
         #LONG인 경우
         if len(piece) > 8:
            first, second = map(piece.split(","))
            result.append(first)
            result.append(second)
         result.append(piece)
         piece = ""

   #마지막 원소는 별도처리
   putHashTag(-1)

   if new_arr[-1] < MAX_BYTE:
      for i in range(MAX_BYTE - len(piece)):
         piece += "."
      result.append(piece)
      piece = ""
   # LONG인 경우
   if len(piece) > 8:
      first, second = map(piece.split(","))
      result.append(first)
      result.append(second)
      piece = ""

   print("["+",".join(result)+"]")