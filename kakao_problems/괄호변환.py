#2020 KAKAO BLIND RECRUITMENT
# u를 결정짓는 마지막 인덱스 반환
def findBalancedIndexLimit(w):
   o, c = 0, 0
   for idx, item in enumerate(w):
      if item == '(':
         o += 1
      else:
         c += 1
      if o == c:
         return idx
   return -1

def isRight(u):
   stack = []
   for i in u:
      if i == '(':
         stack.append(i)
      else:
         if len(stack) == 0:
            return False
         else:
            stack.pop()
   return not stack  # 스택이 비어 있으면 올바름


def recursion(w):
   # 1. 빈 문자열인 경우 반환
   if not w:
      return ""

   # 2. 문자열을 균형잡힌 u, v로 분리
   index = findBalancedIndexLimit(w)
   u = w[:index + 1]
   v = w[index + 1:]

   # 3. u가 올바른 괄호 문자열인지 확인
   if isRight(u):
      return u + recursion(v)
   else:
      result = '('
      result  += recursion(v)
      result += ')'
      u = u[1:-1]
      u = ''.join('(' if char == ')' else ')' for char in u) #괄호 방향 뒤집기
      result += u
      return result


def solution(p):
   return recursion(p)