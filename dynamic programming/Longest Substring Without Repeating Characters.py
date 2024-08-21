#LeetCode, Logest Substring Without Repeating Characters
#투포인터와 구현으로 풀었지만, 슬라이딩 윈도우와 dp로 푼 사람의 솔루션이 더 빠름

class Solution:
   def lengthOfLongestSubstring(self, s:str)->int:
      if len(s) ==0 or len(s)==1:
         return len(s)
      dp = [1]*len(s) # 인덱스 i에서 끝나는 가장 긴 부분 문자열 길이를 저장함.
      for i in range(1, len(s)):
         if s[i] in s[i-dp[i-1]:i]: # s[i]가 이전 부분 문자열에 존재하면
            index = s.index(s[i], i-dp[i-1]) #s[i]의 첫번째 위치를 찾는다
            dp[i] = i-index #문자열 길이
            continue
         dp[i] = dp[i-1]+1 #dp스러운 부분
      return max(dp) #배열
