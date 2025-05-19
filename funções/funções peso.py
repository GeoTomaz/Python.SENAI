def calculadora_imc(peso, altura):
    return peso / altura **2

def classifica_imc(imc):
    if imc < 18.5:
        print("magreza ")
    elif imc > 18.5 and imc <= 24.9:
        print("normal ")
    elif imc > 25 and imc <= 29.9:
        print("sobrepeso ")
    elif imc > 30 and imc <= 34.9:
        print("obesidade 1 ")
    elif imc > 35 and imc <= 39.9:
        print("obesidade 2 ")
    elif imc > 40:
        print("obesidade 3")

peso = float(input("digite seu peso "))
altura = float(input("digite sua altura "))

imc = calculadora_imc(peso, altura)

classifica_imc(imc)

