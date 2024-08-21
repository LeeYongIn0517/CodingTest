#LeetCode 2762번
class Solution:
   def continuousSubarrays(self, nums):
      ans = 1
      left = nums[0] - 2 #현재 서브 배열에서 가능한 가장 작은 값
      right = nums[0] + 2 #현재 서브 배열에서 가능한 가장 큰 값
      l = 0 #왼쪽 포인터

      #nums[l..r]이 유효한 배열인지 확인한다
      for r in range(1, len(nums)): #오른쪽 포인터
         if left <= nums[r] <= right:
            left = max(left, nums[r]-2) #새로 만난 값에 2를 뺀 것과 기존 left 중에 더 큰 걸로
            right = min(right, nums[r]+2) #새로 만난 값에 2를 더한 것과 기존 right중에 더 작은 걸로
         else: #새로 만난 값이 범위에 없으면
            left = nums[r] - 2
            right = nums[r] + 2
            l = r
            while nums[r] - 2 <= nums[l] <= nums[r] + 2:
               left = max(left, nums[l] - 2)
               right = min(right, nums[l] + 2)
               l -= 1
            l += 1 #안 되는 범위까지 온 거니까 그 직전까지 다시 가기 위해 +1해줌(오른쪽으로 옮김)
         ans += r - l + 1 #l에서 까지의 유효한 서브배열의 개수

      return ans
