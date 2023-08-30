def solution(plans):
   plans = sorted(map(lambda x: [x[0], int(x[1][:2]) * 60 + int(x[1][3:]), int(x[2])], plans), key=lambda x: -x[1])

   lst = [] #스택역할
   while plans:
      x = plans.pop()
      print('{0}={1}'.format('x',x))
      for i, v in enumerate(lst):
         print('{0}={1}'.format('v', v))
         #여분의 과제 시간이 현재 시간보다 클 경우
         if v[0] > x[1]:
            lst[i][0] += x[2]
      lst.append([x[1] + x[2], x[0]])
      print('{0}={1}'.format('lst', lst))
   lst.sort()

   return list(map(lambda x: x[1], lst))

print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))