num1 = int(input("digite um numero "))
num2 = int(input("digite um numero "))
num3 = int(input("digite um numero "))

if num1 > num2:
    if num1 > num3:
        print("o número 1 é maior ")
    elif num3 > num2:
        print("o número 3 é maior ")
elif num2 > num3:
    print("o número 2 é maior ")
elif num3 > num1:
    print("o número 3 é maior ")
