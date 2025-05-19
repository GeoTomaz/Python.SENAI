num1 = int(input("escreva um número "))
num2 = int(input("escreva outro número "))
operação = input("escolha uma operação(soma,subtração,multiplicação,divisão)")

soma = num1 + num2
subtração = num1 - num2
multiplicação = num1 * num2
divisão = num1 / num2

if operação == "soma":
    print("o resultado da soma é ", soma)
elif operação == "subtração":
    print("o resultado da subtração é ", subtração)
elif operação == "multiplicação":
    print("o resultado da multiplicação é ", multiplicação)
elif operação == "divisão":
    print("o resultado da divisão é ", divisão)
else:
    print("operação desconhecida ")
    
    
     
                     
    
