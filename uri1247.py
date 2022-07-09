#1247
import math
D, VF, VG = map(int, input().split())
ai = 12
Sub = math.sqrt((ai*ai)+(D*D))
tf = ai/VF
tg = (Sub/VG)
if tg > tf:
    print('N')
else:
    print('S')