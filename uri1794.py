#1794
N = int(input())
LA, LB = input().split()
LA = int(LA)
LB = int(LB)
SA, SB = input().split()
SA = int(SA)
SB = int(SB)

if (N<LA, N<LB, N<SA, N<SB):
   print("possível")
elif (N>LA, N>LB, N>SA, N>SB):
   print("impossivel")