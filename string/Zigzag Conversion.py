#Leet Code
class Solution(object):
   def convert(self, s, numRows):
      ary = [""] * (numRows + 1)
      if numRows == 1:
         return s
      num = numRows - 1
      for i in range(len(s)):
         if int(i / num) % 2 == 0:
            ary[i % num] += s[i]
         else:
            ary[num - i % num] += s[i]

      answer = ""
      for element in ary:
         answer += element
      return answer