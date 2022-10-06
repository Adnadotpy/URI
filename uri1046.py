#1046
I, F = map(int, input().split())

if I < F:
   T = F - I
else:
   T = (24 - I) + F
print("O JOGO DUROU {} HORAS(S)".format(T))