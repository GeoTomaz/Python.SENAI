num = int(input("digite um número "))
n = 0
quantidade = 0
while n <= num:
    if n % 2 == 0:
        print(n)
        quantidade = quantidade + 1
    n = n + 1
print("a quantidade de números pares é ", quantidade)
