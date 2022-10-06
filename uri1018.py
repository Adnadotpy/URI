#1018
n = (input())

n = int(n)
n100 = n//100
falta = n%100
n50 = falta//50
falta = falta%50
n20 = falta//20
falta = falta%20
n10 = falta//10
falta = falta%10
n5 = falta//5
falta = falta%5
n2 = falta//2
falta = falta%2
n1 = falta//1
falta = falta%1

print(n)
print(n100, "nota(s) de R$ 100,00")
print(n50, "nota(s) de R$ 50,00")
print(n20, "nota(s) de R$ 20,00")
print(n10, "nota(s) de R$ 10,00")
print(n5, "nota(s) de R$ 5,00")
print(n2, "nota(s) de R$ 2,00")
print(n1, "nota(s) de R$ 1,00")