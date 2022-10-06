#2702
CA, BA, PA = map(int, input().split())
CR, BR, PR = map(int, input().split())
R = 0

if CR > CA:
   R = R + (CR - CA)
if BR > BA:
   R = R + (BR - BA)
if PR > PA:
   R = R + (PR - PA)
   print(R)