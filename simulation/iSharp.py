#3568번
words = list(map(str,input().split()))
vars,new_vars = words[1:], []
for i,v in enumerate(vars):
   new_vars.append(v[:-1])

for i,v in enumerate(new_vars):
   l,new_word = list(v),''
   n_l = [] #알파벳 제외하고 들어가야함
   alphabet = ''
   for i,v in enumerate(l):
      aschi = ord(v)
      if (aschi >= 65 and aschi <= 90) or (aschi >= 97 and aschi <= 122):
         alphabet += chr(aschi)
      else:
         n_l.append(l[i])

   for idx in range(len(n_l)-1,-1,-1):
      if n_l[idx] == '[':
         new_word += ']'
      elif n_l[idx] == ']':
         new_word += '['
      else:
         new_word += n_l[idx]
   new_word += ' ' + alphabet
   print(words[0]+new_word+';')