def solution(diffs, times, limit):
   answer = max(diffs)
   sorted_diffs = sorted(diffs)
   dp = [i for i in range(min(diffs), max(diffs) + 1)]
   s, e = 0, len(dp) - 1
   while True:
      mid = (s + e) // 2
      level = dp[mid]

      total_time, time_prev, time_cur = 0, 0, 0
      for i, diff in enumerate(diffs):
         solve_time = 0
         time_cur = times[i]
         if diff <= level:
            solve_time = time_cur
         elif diff > level:
            solve_time = (time_cur + time_prev) * (diff - level) + time_cur

         time_prev = time_cur
         total_time += solve_time

      if total_time > limit:  # level을 높여서 다시 반복 ㄱㄱ
         s = mid + 1

      if total_time <= limit:
         e = mid - 1
         answer = min(level, answer)

      if s > e:
         break

   return answer