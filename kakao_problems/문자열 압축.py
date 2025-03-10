def solution(s):
   result = []
   for i in range(1, len(s) + 1):  # i자씩 끊기!
      b = ''
      cnt = 1  # 갯수 체크
      tmp = s[:i]  # 첫번째 미리 자르기

      for j in range(i, len(s) + i, i):  # i부터 끝까지 i단위로 나누어 탐색
         if tmp == s[j:i + j]:  # 앞과 같으면
            cnt += 1  # 카운트
         else:  # 아니면
            if cnt != 1:  # 앞에서 중복이 있었다!
               b = b + str(cnt) + tmp  # 글자 만들기
            else:
               b = b + tmp  # 더하기
            tmp = s[j:j + i]
            cnt = 1  # 앞과 다르므로 중복카운트 초기화
      result.append(len(b))

   return min(result)