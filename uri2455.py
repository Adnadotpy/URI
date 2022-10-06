#2455
P1, C1, P2, C2 = input().split()
P1 = int(P1)
C1 = int(C1)
P2 = int(P2)
C2 = int(C2)

if (P1 * C1 == P2 * C2):
   print("0")
elif (P1 * C1 < P2 * C2):
   print("1")
elif (P1 * C1 > P2 * C2):
   print("-1")