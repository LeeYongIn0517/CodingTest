#LeetCode
class Solution(object):
   def coinChange(self, coins, amount):
      ary = [amount + 1] * (amount + 1)
      ary[0] = 0
      if amount == 0:
         return 0

      for i in range(1, amount + 1):
         for coin in coins:
            if i - coin < 0:
               continue
            ary[i] = min(ary[i], ary[i - coin] + 1)
      answer = -1
      if ary[amount] != amount + 1:
         answer = ary[amount]
      return answer