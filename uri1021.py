#1021
N = float(input())

N100 = N//100
N = N - N100*100
N50 = N//50
N = N - N50*50
N20 = N//20
N = N - N20*20
N10 = N//10
N = N - N10*10
N5 = N//5
N = N - N5*5
N2 = N//2
N = N - N2*2

N1 = N//1
N = N - N1*1
N1 = float("%.2f"%N1)
N = float("%.2f"%N)

M50 = N//0.5
N = N - M50*0.5
M50 = float("%.2f"%M50)
N = float("%.2f"%N)
M25 = N//0.25
N = N - M25*0.25
M25 = float("%.2f"%M25)
N = float("%.2f"%N)
M10 = N//0.10
N = N - M10*0.10
M10 = float("%.2f"%M10)
N = float("%.2f"% N)
M5 = N//0.05
N = N - M5*0.05
M5 = float("%.2f"%M5)
N = float("%.2f"%N)
M1 = N*100
M1 = float("%.2f"%M1)
N = float("%.2f"%N)

print("NOTAS:")
print(N100, "nota(s) de R$ 100.00")
print(N50, "nota(s) de R$ 50.00")
print(N20, "nota(s) de R$ 20.00")
print(N10, "nota(s) de R$ 10.00")
print(N5, "nota(s) de R$ 5.00")
print(N2, "nota(s) de R$ 2.00")

print("MOEDAS:")
print(N1, "moeda(s) de R$ 1.00")
print(M50, "moeda(s) de R$ 0.50")
print(M25, "moeda(s) de R$ 0.25")
print(M10, "moeda(s) de R$ 0.10")
print(M5, "moeda(s) de R$ 0.05")
print(M1, "moeda(s) de R$ 0.01")