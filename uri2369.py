#2369
N = int(input())
C = 7
if N >= 101:
    C += (N - 100) * 5 + 140 + 20
elif N >= 31:
    C += (N - 30) * 2 + 20
elif N >= 11:
    C += N - 10

print(C)