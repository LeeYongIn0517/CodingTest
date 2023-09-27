n,l = int(input()), []
b_list = []
for _ in range(n):
   op,rD,rA,rW = map(str, input().split())
   l.append( (op,int(rD),int(rA),int(rW)) )

def opcodeToBit(v):
   if v == 'ADD':
      return ('0000','0')
   elif v == 'ADDC':
      return ('0000','1')
   elif v == 'SUB':
      return ('0001','0')
   elif v == 'SUBC':
      return ('0001','1')
   elif v == 'MOV':
      return ('0010','0')
   elif v == 'MOVC':
      return ('0010','1')
   elif v == 'AND':
      return ('0011','0')
   elif v == 'ANDC':
      return ('0011','1')
   elif v == 'OR':
      return ('0100','0')
   elif v == 'ORC':
      return ('0100','1')
   elif v == 'NOT':
      return ('0101','0')
   elif v == 'MULT':
      return ('0110','0')
   elif v == 'MULTC':
      return ('0110','1')
   elif v == 'LSFTL':
      return ('0111','0')
   elif v == 'LSFTLC':
      return ('0111','1')
   elif v == 'LSFTR':
      return ('1000', '0')
   elif v == 'LSFTRC':
      return ('1000', '1')
   elif v == 'ASFTR':
      return ('1001', '0')
   elif v == 'ASFTRC':
      return ('1001', '1')
   elif v == 'RL':
      return ('1010', '0')
   elif v == 'RLC':
      return ('1010', '1')
   elif v == 'RR':
      return ('1011', '0')
   elif v == 'RRC':
      return ('1011', '1')

def mapToBit(v,n):
   trash,result = bin(v).split('b')
   if len(result) < n:
      while len(result) < n:
         result = '0' + result
   return result

for i,v in enumerate(l):
   op, rD, rA, rW = v
   bit0_3,bit4 = opcodeToBit(op)
   bit5 = '0'
   bit6_8 = mapToBit(rD,3)

   bit9_11 = ''
   if op == 'NOT' or op == 'MOV' or op == 'MOVC':
      bit9_11 = '000'
   else:
      bit9_11 = mapToBit(rA,3)

   lastBit = ''
   if bit4 == '0':
      bit12_14 = mapToBit(rW,3)
      lastBit = bit12_14+'0'
   else:
      lastBit = mapToBit(rW, 4)

   b_list.append(bit0_3+bit4+bit5+bit6_8+bit9_11+lastBit)

for i,v in enumerate(b_list):
   print(v)