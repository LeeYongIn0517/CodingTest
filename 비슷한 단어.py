import sys
input = sys.stdin.readline
n = int(input().rstrip())
alpha = [[] for _ in range(26)]
#첫 알파벳으로 분류
for _ in range(n):
   str = input().rstrip()
   fir_str = str[0]
   idx = ord(fir_str) - 97
   alpha[idx].append(str)

dict = {}
#2개 이상인 거만 비교
for i in range(26):
   if len(alpha[i]) >= 2:
      alpha[i].sort(key = lambda x:(len(x)))
      answer = 0 #임시 값
      word = []
      lcs = 0  # 최종값
      for k in range(len(alpha[i])-1):
         string_a = alpha[i][k]

         for j in range(k+1 ,len(alpha[i])):
            string_b = alpha[i][j]
            for h in range(len(string_b)):
               if h < len(string_a):
                  if string_a[h] == string_b[h]:
                     answer += 1

            if lcs < answer: #갱신
               lcs = answer
               word = [string_a, string_b]
               dict[alpha[i]] = (answer,word)
            answer = 0 #초기화
print(dict)