l1 = int(input("digite um número "))
l2 = int(input("digite um número "))
l3 = int(input("digite um número "))


if l1 == l2 == l3:
    print("é um triângulo equilátero ")
if l1 == l2 and l1 != l3 or l1 == l3 and l1 != l2 or l3 == l2 and l3 != l1:
    print("é um triângulo isósceles ")
if l1 != l2 and l1 != l3 and l2 != l3:
    print("é um triângulo escaleno ")