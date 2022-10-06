#1046
A = input().split()
HI, HF = A
HI = int(A[0])
HF = int(A[1])

if HI < HF:
   T = HF - HI
else:
   T = (24 - HI) + HF
   
print("O JOGO DUROU {} HORAS(S)".format(T))