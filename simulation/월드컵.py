#6987번
l = []
answer = ['1','1','1','1']
for li in range(4):
   tmp = list(map(int,input().split()))
   l.append(tmp)

for i,tmp in enumerate(l):
   round_total_win, round_total_lose = 0,0
   round_mu_list = [tmp[1],tmp[4],tmp[7],tmp[10],tmp[13],tmp[16]]

   for mi,mv in enumerate(round_mu_list):
      idx = mi+1
      while round_mu_list[mi] > 0 and idx < 6:
         if round_mu_list[idx] > 0:
            round_mu_list[mi] -= 1
            round_mu_list[idx] -= 1
         idx += 1

   for a,b in enumerate(round_mu_list):
      flag = False
      if b != 0:
         answer[i] = '0'
         flag = True
      if flag:
         break

   for j in range(0,6):
      win, mu, lose = tmp[3*j],tmp[3*j+1],tmp[3*j+2]
      round_total_win += win
      round_total_lose += lose
      flag = False
      if win+mu+lose < 5:
         answer[i] = '0'
         flag = True
      if flag:
         break

   if round_total_win != round_total_lose:
      answer[i] = '0'

print(' '.join(answer))
