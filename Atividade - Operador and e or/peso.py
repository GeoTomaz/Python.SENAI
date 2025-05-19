imc1 = int(input("digite seu peso "))
imc2 = float(input("digite sua altura "))

multiplicação = imc2 * imc2
calculo_imc = imc1 / multiplicação

if calculo_imc < 18.5:
    print("abaixo do peso ")
elif calculo_imc >= 18.5 and calculo_imc <= 24.9:
    print("peso normal ")
elif calculo_imc >= 25 and calculo_imc <= 29.9:
    print("sobrepeso ")
elif calculo_imc >= 30 and calculo_imc <= 34.9:
    print("obesidade 1 ")
elif calculo_imc >= 35 and calculo_imc <= 39.9:
    print("obesidade 2 ")
else:
    print("obesidade 3 ")